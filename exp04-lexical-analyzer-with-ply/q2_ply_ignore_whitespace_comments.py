# Q2. Ignore whitespace, tabs and comments (// single-line and
#     /* multi-line */) in the input source program using PLY.
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

# Whitespace and tabs are ignored
t_ignore = ' \t'


def t_COMMENT_SINGLE(t):
    r'//.*'
    pass  # comment - no token returned


def t_COMMENT_MULTI(t):
    r'/\*[\s\S]*?\*/'
    t.lexer.lineno += t.value.count('\n')
    pass  # comment - no token returned


def t_NUMBER(t):
    r'\d+\.\d+|\d+'
    t.value = float(t.value) if '.' in t.value else int(t.value)
    return t


def t_IDENTIFIER(t):
    r'[a-zA-Z][a-zA-Z0-9]*'
    return t


def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)


def t_error(t):
    print(f"Illegal character '{t.value[0]}'")
    t.lexer.skip(1)


lexer = lex.lex()

data = """
// single-line comment
x = 10 + 5   /* multi-line
comment continues */
y = x * 2
"""
lexer.input(data)
for tok in lexer:
    print(tok.type, tok.value)
