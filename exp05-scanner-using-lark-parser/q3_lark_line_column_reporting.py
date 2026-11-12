# Q3. Line and column number reporting using Lark token metadata.
# Install first: pip install lark

from lark import Lark, Token

grammar = r"""
start: WORD+
WORD: /[a-zA-Z_]+/
%ignore WS
WS: /[ \t\n]+/
"""

parser = Lark(grammar, parser="lalr", propagate_positions=True)
data = "hello world\ncompiler lab"
tree = parser.parse(data)
for token in tree.scan_values(lambda v: isinstance(v, Token)):
    print(f"{token.type} : {token.value} @ line {token.line}, column {token.column}")
