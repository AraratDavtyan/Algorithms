def build_transition_table(pattern):
    m = len(pattern)
    unique_chars = set(pattern)
    transition_table = {}

    for state in range(m + 1):
        transitions = {ch: 0 for ch in unique_chars}
        transition_table[state] = transitions

    for state in range(m + 1):
        for ch in unique_chars:
            transition_table[state][ch] = compute_next_state(pattern, state, ch)

    return transition_table, unique_chars


def compute_next_state(pattern, current_state, char):
    m = len(pattern)
    if current_state < m and char == pattern[current_state]:
        return current_state + 1
    for ns in range(current_state, 0, -1):
        if pattern[ns - 1] == char:
            return ns
    return 0


def finite_automata_search(text, pattern):
    m = len(pattern)
    n = len(text)

    transition_table, unique_chars = build_transition_table(pattern)

    current_state = 0
    for i in range(n):
        if text[i] in unique_chars:
            current_state = transition_table[current_state][text[i]]
        else:
            current_state = 0  

        if current_state == m:
            print(f"Pattern found at index {i - m + 1}")
            current_state = 0  


print("\nFinite Automata String Matching Example:")
finite_automata_search("sdsdcfklkooop", "op")
