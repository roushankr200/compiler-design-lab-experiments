# Q5. Token categorization and file storage in Lark:
#     identifiers.txt, numbers.txt, operators.txt, keywords.txt + frequency report.
# NOTE (fixes): the handout grammar (start: WORD+ / WORD: ...) yields no tokens
# when scanned, so a lowercase token rule is used; KEYWORD gets priority .2 so
# "int"/"return" lex as KEYWORD instead of IDENTIFIER.
# Install first: pip install lark

from lark import Lark, Token
from collections import Counter

grammar = r"""
start: token+
token: IDENTIFIER | NUMBER | OPERATOR | KEYWORD
IDENTIFIER: /[a-zA-Z_][a-zA-Z0-9_]*/
NUMBER: /\d+(\.\d+)?/
OPERATOR: "+" | "-" | "*" | "/" | "="
KEYWORD.2: "int" | "float" | "if" | "else" | "while" | "return"
%ignore WS
WS: /[ \t\n]+/
"""

parser = Lark(grammar, parser="lalr", propagate_positions=True)
data = "int x = 10 x = x + 5 return x"
tree = parser.parse(data)

ids, nums, ops, keys = [], [], [], []
for token in tree.scan_values(lambda v: isinstance(v, Token)):
    if token.type == "IDENTIFIER":
        ids.append(token.value)
    elif token.type == "NUMBER":
        nums.append(token.value)
    elif token.type == "OPERATOR":
        ops.append(token.value)
    elif token.type == "KEYWORD":
        keys.append(token.value)

open("identifiers.txt", "w").write("\n".join(ids))
open("numbers.txt", "w").write("\n".join(nums))
open("operators.txt", "w").write("\n".join(ops))
open("keywords.txt", "w").write("\n".join(keys))

print("Identifier Frequency:", Counter(ids))
print("Number Frequency:", Counter(nums))
print("Operator Frequency:", Counter(ops))
print("Keyword Frequency:", Counter(keys))
