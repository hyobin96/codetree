n = int(input())
arr = [input().split() for _ in range(n)]

def count_cnt(i, j, k):
    s = str(i) + str(j) + str(k)
    for e in arr:
        cnt1, cnt2 = 0, 0
        for a, b in zip(e[0], s):
            if a == b:
                cnt1 += 1
            elif a in s:
                cnt2 += 1
        if cnt1 != int(e[1]) or cnt2 != int(e[2]):
            return False
    return True
cnt = 0
for i in range(1, 10):
    for j in range(1, 10):
        for k in range(1, 10):
            if i == j or j == k or i == k:
                continue
            if count_cnt(i, j, k):
                cnt += 1

print(cnt)