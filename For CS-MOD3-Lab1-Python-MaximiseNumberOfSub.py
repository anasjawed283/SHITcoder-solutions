def maximum_subsequence_count(text, pattern):
    res = 0
    cnt1 = 0
    cnt2 = 0

    for c in text:
        if c == pattern[1]:
            res += cnt1
            cnt2 += 1
        if c == pattern[0]:
            cnt1 += 1

    return res + max(cnt1, cnt2)

# Input
text = input()
pattern = input()

# Output
result = maximum_subsequence_count(text, pattern)
print(result)
