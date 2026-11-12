# Q5. Handle lexical errors gracefully using PLY:
#     detect illegal characters, print the line and column number
#     of the error, skip the invalid character and continue scanning.
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
t_ignore = ' \t'


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


def find_column(input_text, token):
    last_newline = input_text.rfind('\n', 0, token.lexpos)
    if last_newline < 0:
        last_newline = -1
    return token.lexpos - last_newline


def t_error(t):
    column = find_column(t.lexer.lexdata, t)
    print(f"Lexical Error: Illegal character '{t.value[0]}' "
          f"at line {t.lineno}, column {column}")
    t.lexer.skip(1)  # skip the invalid character and continue


lexer = lex.lex()

data = "x = 10 + $5\ny = #20 + 3"
lexer.input(data)
for tok in lexer:
    print(tok.type, tok.value)
print("Scanning completed (errors were skipped, scanning continued).")
