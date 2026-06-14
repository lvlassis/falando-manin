import unittest
import sys
import os

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

from verso.tokenization import tokenization
from verso.tokens import Token


class TestDeclaracao(unittest.TestCase):

    def test_declaracao_simples(self):
        # Amor é Rocha. -> int amor;
        tokens = tokenization("Amor é Rocha.")
        self.assertEqual(tokens[0], Token(type='VARIABLE', value='amor'))
        self.assertEqual(tokens[1], Token(type='DECLARATION', value=''))
        self.assertEqual(tokens[2], Token(type='PRIMITIVE_TYPE', value='int'))
        self.assertEqual(tokens[3], Token(type='DOT', value='.'))

    def test_declaracao_com_valor(self):
        # Amor é Rocha forte. -> int amor = 10;
        tokens = tokenization("Amor é Rocha forte.")
        self.assertEqual(tokens[2], Token(type='PRIMITIVE_TYPE', value='int'))
        self.assertEqual(tokens[3], Token(type='NUMERIC_EXPRESSION', value='forte'))

    def test_comentario(self):
        tokens = tokenization("# int amor;")
        self.assertEqual(len(tokens), 1)
        self.assertEqual(tokens[0].type, 'COMMENT')


class TestTiposPrimitivos(unittest.TestCase):

    def test_int_rocha(self):
        tokens = tokenization("Vida é Rocha.")
        tipo = next(t for t in tokens if t.type == 'PRIMITIVE_TYPE')
        self.assertEqual(tipo.value, 'int')

    def test_float_bruma(self):
        tokens = tokenization("Paixão é bruma.")
        tipo = next(t for t in tokens if t.type == 'PRIMITIVE_TYPE')
        self.assertEqual(tipo.value, 'float')

    def test_float_nevoa(self):
        tokens = tokenization("Paixão é névoa.")
        tipo = next(t for t in tokens if t.type == 'PRIMITIVE_TYPE')
        self.assertEqual(tipo.value, 'float')

    def test_char_suspiro(self):
        tokens = tokenization("A vida é um suspiro.")
        tipo = next(t for t in tokens if t.type == 'PRIMITIVE_TYPE')
        self.assertEqual(tipo.value, 'char')

    def test_string_verso(self):
        tokens = tokenization("Que o amor seja um verso.")
        tipo = next(t for t in tokens if t.type == 'PRIMITIVE_TYPE')
        self.assertEqual(tipo.value, 'char[]')


if __name__ == '__main__':
    unittest.main()
