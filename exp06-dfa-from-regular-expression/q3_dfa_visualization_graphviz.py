# Q3. DFA visualization using Graphviz (for regex a*b).
# Install first: pip install graphviz
# Also needs the Graphviz 'dot' program installed on the system.
# Renders dfa_a_star_b.pdf (and opens it when view=True).

from graphviz import Digraph

dot = Digraph()

# States
dot.node('q0', 'q0 (Start)')
dot.node('q1', 'q1 (Final)', shape='doublecircle')

# Transitions
dot.edge('q0', 'q0', label='a')
dot.edge('q0', 'q1', label='b')

dot.render('dfa_a_star_b', view=True)
print("DFA diagram rendered as dfa_a_star_b.pdf")
