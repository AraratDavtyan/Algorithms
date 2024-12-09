def longest_palindromic_substring(string):
    def expand_around_center(s, left, right):
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
        return s[left + 1:right]

    longest = ""
    for i in range(len(string)):
        temp = expand_around_center(string, i, i)
        if len(temp) > len(longest):
            longest = temp
        temp = expand_around_center(string, i, i + 1)
        if len(temp) > len(longest):
            longest = temp
    return longest
