from collections import defaultdict

length, s = input().rstrip().split()
length = int(length)

p = [31, 37]
m = [int(1e9) + 7, int(1e9) + 9]

p_pow = [[0] * (length + 1) for _ in range(2)]
for k in range(2):
    p_pow[k][0] = 1
    for i in range(1, length + 1):
        p_pow[k][i] = (p_pow[k][i - 1] * p[k] + m[k]) % m[k]

to_int = lambda c: ord(c) - ord('a') + 1

s_hash = [0] * 2
for k in range(2):
    for i in range(length):
        s_hash[k] = (s_hash[k] + to_int(s[i]) * p_pow[k][length - i - 1] + m[k]) % m[k]

d = defaultdict(int)
d[(s_hash[0], s_hash[1])] = 1

for i in range(1, len(s) - length + 1):
    for k in range(2):
        s_hash[k] = (s_hash[k] * p[k] - to_int(s[i - 1]) * p_pow[k][length] + to_int(s[i + length - 1]) + m[k]) % m[k]

    d[(s_hash[0], s_hash[1])] += 1

answer = max(d.values())
print(answer)

