from collections import defaultdict

s = input().rstrip()

s_length = len(s)
p = [31, 37]
m = [int(1e9) + 7, int(1e9) + 9]
to_int = lambda c: ord(c) - ord('a') + 1

s_int = [0] * s_length
for i, c in enumerate(s):
    s_int[i] = to_int(c)

def is_possible(length):
    p_pow = [[0] * (length + 1) for _ in range(2)]
    for k in range(2):
        p_pow[k][0] = 1
        for i in range(1, length + 1):
            p_pow[k][i] = (p_pow[k][i - 1] * p[k]) % m[k]
    
    d = defaultdict(int)
    hash = [0, 0]
    for k in range(2):
        for i in range(length):
            hash[k] = (hash[k] + s_int[i] * p_pow[k][length - i - 1]) % m[k]
    
    d[(hash[0], hash[1])] = 1
    
    for i in range(1, s_length - length + 1):
        for k in range(2):
            hash[k] = (hash[k] * p[k] - s_int[i - 1] * p_pow[k][length] + s_int[i + length - 1] + m[k]) % m[k]
        d[(hash[0], hash[1])] += 1
        if d[(hash[0], hash[1])] == 2:
            return True
    return False
    


max_length = 0
l, r = 0, (s_length // 2 + 1)
while l <= r:
    mid = (l + r) // 2
    if is_possible(mid):
        l = mid + 1
        max_length = max(max_length, mid)
    else:
        r = mid - 1

print(max_length)