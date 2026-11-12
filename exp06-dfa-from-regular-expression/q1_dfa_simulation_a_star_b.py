# Q1. Simple DFA simulation for the regular expression: a*b
# States: q0 (start), q1 (final)

dfa = {
    'q0': {'a': 'q0', 'b': 'q1'},
    'q1': {}
}
start_state = 'q0'
final_states = ['q1']


def simulate_dfa(string):
    state = start_state
    for char in string:
        if char in dfa[state]:
            state = dfa[state][char]
        else:
            return False
    return state in final_states


# Test strings
test_strings = ["b", "ab", "aaab", "a", "abb"]
for s in test_strings:
    print(s, "->", "Accepted" if simulate_dfa(s) else "Rejected")
