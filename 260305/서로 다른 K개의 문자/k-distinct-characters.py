import sys
input = sys.stdin.readline

string, k = input().split()
n = len(string)
k = int(k)

alpha_map = dict()
j = 0
max_length = 1
alpha_map[string[j]] = alpha_map.get(string[j], 0) + 1
for i in range(n):
    
    while j + 1 < n and len(alpha_map) <= k:
        s = string[j + 1]
        alpha_map[s] = alpha_map.get(s, 0) + 1
        if len(alpha_map) > k:
            del alpha_map[s]
            break
        j += 1

    if len(alpha_map) <= k:
        max_length = max(max_length, j - i + 1)

    alpha_map[string[i]] -= 1
    if alpha_map[string[i]] == 0:
        del alpha_map[string[i]]

print(max_length)