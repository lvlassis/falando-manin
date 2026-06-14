from dataclasses import dataclass
from os import error
from typing import List

@dataclass
class Token:
    type: str
    value: str|None = None

TOKEN_WEAK = 'WEAK'
TOKEN_DOT = 'DOT'
TOKEN_COMMENT = 'COMMENT'
TOKEN_DECLARATION = 'DECLARATION'
TOKEN_VARIABLE = 'VARIABLE'
TOKEN_EOL = 'EOL'
TOKEN_PRIMITIVE_TYPE = 'PRIMITIVE_TYPE'
TOKEN_NUMERICAL_EXPRESSION = 'NUMERICAL_EXPRESSION'

# Tipos
TYPE_INTEGER = "INTEGER"


TOKEN_TYPES = [
    'DECLARATION'
    'PRIMITIVE_TYPE'
    'DOT'
    'COMMENT'

    'VARIABLE'
    'NUMERIC_EXPRESSION'
]


def filter_comments(line: str) -> str:
    """ Remove os comentários de uma linha """
    return line.split("#")[0].strip()


def verso_split(line: str) -> list[str]:
    """ Realiza a separação inicial em uma linha """
    line = line.strip()
    words = []
    start = 0
    for i, c in enumerate(line):
        if c == " ":
            words.append(line[start:i+1])
            start = i+1
        elif c == ".":
            words.append(line[start:i])
            words.append(".")
            start = i+1
    return words


def tokenize(program: str) -> list[Token]:
    """ Função que realiza a etapa de tokenização """

    tokens = []
    lines = program.splitlines()
    for line in lines:
        line = filter_comments(line)
        words = verso_split(line)

        line_tokens = []

        # Tokenize Weak
        for word in words:
            token = tokenize_word_weak(word)
            if token.type == TOKEN_COMMENT:
                break
            line_tokens.append(token)

        # Tokenize Strong
        line_tokens = tokenize_strong(line_tokens)
        for token in line_tokens:
            tokens.append(token)
        tokens.append(Token(TOKEN_EOL))
        

    return tokens


def find_next(tipo: str, tokens: list[Token]) -> tuple[Token, int] | None:
    return next(((t, i) for i, t in enumerate(tokens) if t.type == tipo), None)

def group_tokens(tokens: list[Token], token_type = TOKEN_WEAK):
    value = ""
    for i, t in enumerate(tokens):
        if t.value:
            value += t.value
        if i != len(tokens) - 1:
            value += " "
    return Token(token_type, value)


def tokenize_word_weak(word: str) -> Token:
    """ Tokeniza uma palavra individualmente """
    word = word.strip().lower()
    if word == ".":
        return Token(TOKEN_DOT)
    elif word == "é":
        return Token(TOKEN_DECLARATION)
    elif word == "rocha":
        return Token(TOKEN_PRIMITIVE_TYPE, TYPE_INTEGER)
    return Token(TOKEN_WEAK, word)


def tokenize_strong(line_tokens: List[Token]) -> List[Token]:
    """ Classifica os Tokens Fracos com base na sintaxe """
    
    # Encontra os tokens classificados
    tokens_classificados = []
    for i, token in enumerate(line_tokens):
        if token.type != TOKEN_WEAK:
            tokens_classificados.append((token, i))
    
    # Busca se a linha possui alguma declaração de variável
    result = next(((t, i) for t, i in tokens_classificados if t.type == TOKEN_DECLARATION), None)
    if result:
        # Classifica a variável
        _, pos = result
        line_tokens[pos-1].type = TOKEN_VARIABLE

        # Classifica os tokens de value
        if line_tokens[pos+1].type != TOKEN_PRIMITIVE_TYPE:
             raise error("Erro de sintaxe, esperado token de tipo primitivo")

        if line_tokens[pos+1].value == TYPE_INTEGER:
            final = find_next(TOKEN_DOT, line_tokens)
            if not final:
                final = find_next(TOKEN_EOL, line_tokens)
            if final:
                _, i = final
                numerical_tokens = line_tokens[pos+2:i]
                numerical_token = group_tokens(numerical_tokens, TOKEN_NUMERICAL_EXPRESSION)
                for j in range(i-1, pos+1,  -1):
                    line_tokens.pop(j)
                line_tokens.insert(pos+2, numerical_token)

    return line_tokens


