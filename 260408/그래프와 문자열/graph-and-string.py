import sys
sys.setrecursionlimit(100_000)

node_count, s = input().rstrip().split()
node_count = int(node_count)
length = len(s)
to_int = lambda c: ord(c) - ord('a') + 1

tree = [[] for _ in range(node_count + 1)]
for _ in range(node_count - 1):
    u, v, c = input().rstrip().split()
    tree[int(u)].append((int(v), to_int(c)))

p = [31, 37]
m = [int(1e9) + 7, int(1e9) + 9]

p_pow = [[0] * (length + 1) for _ in range(2)]
for k in range(2):
    p_pow[k][0] = 1
    for i in range(1, length + 1):
        p_pow[k][i] = (p_pow[k][i - 1] * p[k]) % m[k]

t_hash = [0, 0]
for k in range(2):
    for i in range(length):
        t_hash[k] = (t_hash[k] + to_int(s[i]) * p_pow[k][length - i - 1]) % m[k]

d = dict()
d[(t_hash[0], t_hash[1])] = 0
# print(t_hash)
def dfs(curr, s_list, hash):
    # print(s_list, hash)
    if s_list and len(s_list) < length:
        for k in range(2):
            hash[k] = (hash[k] + s_list[-1] * p_pow[k][-len(s_list) - 1]) % m[k]
    elif s_list and len(s_list) >= length:
        if (hash[0], hash[1]) in d:
            d[(hash[0], hash[1])] += 1
        for k in range(2):
            hash[k] = hash[k] * p[k] - s_list[-length] * p_pow[k][length] + m[k]

    for nxt, c in tree[curr]:
        s_list.append(c)
        tmp_hash = hash[:]
        if len(s_list) >= length:
            for k in range(2):
                tmp_hash[k] = (tmp_hash[k] + c) % m[k]

        dfs(nxt, s_list, tmp_hash)
        s_list.pop()

dfs(1, [], [0, 0])
answer = max(d.values())
print(answer)