# Q3. Restrict identifier length to 10 characters and print an
#     error message if an identifier exceeds this limit.
# Install first: pip install ply

import ply.lex as lex

tokens = (
    'IDENTIFIER',
    'NUMBER',
    'EQUALS',
)

t_EQUALS = r'='
t_ignore = ' \t\n'

MAX_IDENTIFIER_LENGTH = 10


def t_IDENTIFIER(t):
    r'[a-zA-Z][a-zA-Z0-9]*'
    if len(t.value) > MAX_IDENTIFIER_LENGTH:
        print(f"Error: Identifier '{t.value}' exceeds the maximum "
              f"length of {MAX_IDENTIFIER_LENGTH} characters")
        return None  # identifier not returned as a token
    return t


def t_NUMBER(t):
    r'\d+'
    t.value = int(t.value)
    return t


def t_error(t):
    print(f"Illegal character '{t.value[0]}'")
    t.lexer.skip(1)


lexer = lex.lex()

data = "count = 10 verylongidentifiername = 20 total = 30"
lexer.input(data)
for tok in lexer:
    print(tok.type, tok.value)
