# Q1. Lexical analyzer using PLY that recognizes:
#     Identifiers (letters followed by letters/digits),
#     Numbers (integers and floats),
#     Arithmetic operators (+, -, *, /) and Assignment operator (=)
# Install first: pip install ply

import ply.lex as lex

tokens = (
    'IDENTIFIER',
    'NUMBER',
    'PLUS', 'MINUS', 'TIMES', 'DIVIDE',
    'EQUALS',
)

t_PLUS = r'\+'
t_MINUS = r'-'
t_TIMES = r'\*'
t_DIVIDE = r'/'
t_EQUALS = r'='
t_ignore = ' \t\n'


def t_NUMBER(t):
    r'\d+\.\d+|\d+'
    t.value = float(t.value) if '.' in t.value else int(t.value)
    return t


def t_IDENTIFIER(t):
    r'[a-zA-Z][a-zA-Z0-9]*'
    return t


def t_error(t):
    print(f"Illegal character '{t.value[0]}'")
    t.lexer.skip(1)


lexer = lex.lex()

data = "total = price + 10 * 2 - 3.5 / rate"
lexer.input(data)
for tok in lexer:
    print(tok.type, tok.value)
