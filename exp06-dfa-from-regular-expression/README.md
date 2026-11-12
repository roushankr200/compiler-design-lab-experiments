# Experiment 6 - DFA Creation and Simulation from Regular Expression

Construct and simulate a DFA (here for the regex `a*b`) and visualize it.
Install first: `pip install networkx graphviz` (plus matplotlib for Q2;
Q3 also needs the Graphviz `dot` program installed on the system).

| File | Question |
|---|---|
| q1_dfa_simulation_a_star_b.py | Q1. DFA simulation for a*b - b / ab / aaab Accepted, a / abb Rejected |
| q2_dfa_visualization_networkx.py | Q2. Draw the DFA with NetworkX (saves dfa_networkx.png) |
| q3_dfa_visualization_graphviz.py | Q3. Draw the DFA with Graphviz (renders dfa_a_star_b.pdf; q0 = start, q1 = final, double-circle) |

Run: `python3 q1_dfa_simulation_a_star_b.py` (etc.)
