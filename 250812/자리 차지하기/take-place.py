from sortedcontainers import SortedSet

n, m = map(int, input().split())
arr = list(map(int, input().split()))

s = SortedSet(range(-m, 0))

answer = 0
for a in arr:
    a = -a
    if a not in s:
        idx = s.bisect_right(a)
        if idx == len(s):
            break
        else:
            s.remove(a + 1)
    else:
        s.remove(a)
    
    answer += 1

print(answer)

