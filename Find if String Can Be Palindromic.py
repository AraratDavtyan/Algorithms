def can_be_palindromic(string):
    from collections import Counter
    counts = Counter(string)
    odd_count = sum(1 for count in counts.values() if count % 2 != 0)
    return odd_count <= 1
