# Q2. Ignoring whitespace and comments (// and /* */) in Lark.
# Install first: pip install lark
# NOTE (fix): start allows one OR MORE assignments - the sample data has two
# statements (x = 10; and y = 20;), a single-assignment start did not parse it.

from lark import Lark

grammar = r"""
start: assignment+
assignment: IDENTIFIER "=" NUMBER ";"
IDENTIFIER: /[a-zA-Z_][a-zA-Z0-9_]*/
NUMBER: /\d+/
%ignore WS
%ignore /\/\/.*/
%ignore /\/\*[\s\S]*?\*\//
WS: /[ \t\n]+/
"""

parser = Lark(grammar, parser="lalr")
data = """
// single line comment
x = 10; /* multi-line comment */
y = 20;
"""
print(parser.parse(data))
print("Only valid statements are parsed; comments and spaces are ignored.")
