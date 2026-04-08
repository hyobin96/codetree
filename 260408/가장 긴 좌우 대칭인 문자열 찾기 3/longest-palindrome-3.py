_, c = input().split()
s = input().rstrip()
s = '#' + '#'.join(s) + '#'
s_length = len(s)

center, r = -1, -1
A = [0] * s_length

for i in range(s_length):
    if s[i] == c:
        continue

    if i <= r:
        A[i] = min(A[center * 2 - i], r - i)
    
    while i - A[i] - 1 >= 0 and i + A[i] + 1 < s_length and \
        s[i - A[i] - 1] == s[i + A[i] + 1] != c:
        A[i] += 1
    
    if i + A[i] > r:
        center, r = i, i + A[i]

print(max(A))