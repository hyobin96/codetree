_, query_count = map(int, input().split())
s = input().rstrip()
querys = [tuple(map(int, input().split())) for _ in range(query_count)]
s = '#' + '#'.join(s) + '#'
s_length = len(s)

center, r = -1, -1
A = [0] * s_length
for i in range(s_length):
    if i <= r:
        A[i] = min(A[center * 2 - i], r - i)

    while i - A[i] - 1 >= 0 and i + A[i] + 1 < s_length and \
        s[i - A[i] - 1] == s[i + A[i] + 1]:
        A[i] += 1

    if i + A[i] > r:
        center, r = i, i + A[i]

for a, b in querys:
    size = b - a + 1
    a = a * 2 - 1
    b = b * 2 - 1
    if A[(a + b) // 2] >= size:
        print("Yes")
    else:
        print("No")
