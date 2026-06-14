from verso.tokens import tokenize, verso_split

def test_tokenize():
    programa = """amor é rocha que quando quebra doi no peito. # Comentário"""

    tokens = tokenize(programa)
    print(tokens)

def test_verso_split():
    line = "amor é fogo que arde sem se ver."
    tokens_1 = verso_split(line)
    print(tokens_1)

test_tokenize()

