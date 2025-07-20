N = int(input())
strings = [input() for _ in range(N)]

max_count = 0
d = {}
for s in strings:
    if s in d:
        d[s] += 1
    else:
        d[s] = 1
        
    max_count = max(max_count, d[s])

print(max_count)
    