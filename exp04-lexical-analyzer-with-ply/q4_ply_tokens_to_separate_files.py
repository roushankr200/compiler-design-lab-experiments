# Q4. Store tokens in separate files based on their type:
#     keywords.txt, identifiers.txt, operators.txt, numbers.txt
# Install first: pip install ply

import ply.lex as lex

reserved = {
    'int': 'KEYWORD', 'float': 'KEYWORD', 'if': 'KEYWORD',
    'else': 'KEYWORD', 'while': 'KEYWORD', 'return': 'KEYWORD',
}

tokens = (
    'KEYWORD',
    'IDENTIFIER',
    'NUMBER',
    'OPERATOR',
)

t_ignore = ' \t\n'


def t_OPERATOR(t):
    r'\+|-|\*|/|=|==|!=|<=|>=|<|>'
    return t


def t_NUMBER(t):
    r'\d+\.\d+|\d+'
    return t


def t_IDENTIFIER(t):
    r'[a-zA-Z][a-zA-Z0-9]*'
    t.type = reserved.get(t.value, 'IDENTIFIER')
    return t


def t_error(t):
    print(f"Illegal character '{t.value[0]}'")
    t.lexer.skip(1)


lexer = lex.lex()

data = "int total = 10 if total > 5 return total + 2.5"
lexer.input(data)

buckets = {'KEYWORD': [], 'IDENTIFIER': [], 'OPERATOR': [], 'NUMBER': []}
for tok in lexer:
    buckets[tok.type].append(str(tok.value))
    print(tok.type, tok.value)

open("keywords.txt", "w").write("\n".join(buckets['KEYWORD']))
open("identifiers.txt", "w").write("\n".join(buckets['IDENTIFIER']))
open("operators.txt", "w").write("\n".join(buckets['OPERATOR']))
open("numbers.txt", "w").write("\n".join(buckets['NUMBER']))
print("Tokens stored in keywords.txt, identifiers.txt, operators.txt, numbers.txt")
