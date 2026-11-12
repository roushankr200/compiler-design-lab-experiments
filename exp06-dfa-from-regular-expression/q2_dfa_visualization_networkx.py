# Q2. DFA visualization using NetworkX (for regex a*b).
# Install first: pip install networkx matplotlib
# Also saves the diagram as dfa_networkx.png (plt.show() alone leaves no file).

import networkx as nx
import matplotlib.pyplot as plt

# DFA structure
dfa = {
    'q0': {'a': 'q0', 'b': 'q1'},
    'q1': {}
}

G = nx.DiGraph()

# Add edges
for state, transitions in dfa.items():
    for symbol, next_state in transitions.items():
        G.add_edge(state, next_state, label=symbol)

# Draw graph
pos = nx.spring_layout(G)
nx.draw(G, pos, with_labels=True, node_color='lightblue', node_size=2000)
edge_labels = nx.get_edge_attributes(G, 'label')
nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)

plt.title("DFA for Regular Expression a*b")
plt.savefig("dfa_networkx.png")
plt.show()
print("DFA diagram saved as dfa_networkx.png")
