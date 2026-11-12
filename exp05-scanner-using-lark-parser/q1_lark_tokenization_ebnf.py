# Q1. Tokenization using EBNF grammar in Lark.
# Install first: pip install lark
# NOTE (fix): statement also allows an optional KEYWORD before the identifier
# (e.g. "int x = 10;") - with only IDENTIFIER the sample data did not parse.
# KEYWORD has priority .2 so "int" lexes as KEYWORD, not as an IDENTIFIER.

from lark import Lark

grammar = r"""
?start: statement+

statement: KEYWORD? IDENTIFIER "=" expr ";"
?expr: term (OP term)*
?term: NUMBER | IDENTIFIER
KEYWORD.2: "int" | "float" | "if" | "else" | "while" | "return"
IDENTIFIER: /[a-zA-Z_][a-zA-Z0-9_]*/
NUMBER: /\d+(\.\d+)?/
OP: "+" | "-" | "*" | "/" | "==" | "!=" | "<" | ">" | "<=" | ">="
DELIM: "(" | ")" | "{" | "}" | ";" | ","
%ignore WS
WS: /[ \t\n]+/
"""

parser = Lark(grammar, parser="lalr")
data = "int x = 10; y = x + 3.14;"
tree = parser.parse(data)
for token in tree.scan_values(lambda v: hasattr(v, 'type')):
    print(token.type, token.value)
