s = input().rstrip()

length = len(s)
to_int = lambda c: ord(c) - ord('a') + 1
s_int = [0] * length
for i, c in enumerate(s):
    s_int[i] = to_int(c)

p = [31, 37]
m = [int(1e9) + 1, int(1e9) + 9]

p_pow = [[0] * (length + 1) for _ in range(2)]
for k in range(2):
    p_pow[k][0] = 1
    for i in range(1, length + 1):
        p_pow[k][i] = (p_pow[k][i - 1] * p[k]) % m[k]

count = 0
for l in range(1, length + 1):
    s = set()
    hash = [0, 0]
    for k in range(2):
        for i in range(l):
            hash[k] = (hash[k] + s_int[i] * p_pow[k][l - i - 1]) % m[k]
    s.add((hash[0], hash[1]))
    for i in range(1, length - l + 1):
        for k in range(2):
            hash[k] = (hash[k] * p[k] - s_int[i - 1] * p_pow[k][l] + s_int[i + l - 1] + m[k]) % m[k]
        s.add((hash[0], hash[1]))
    count += len(s)

print(count)
    
