n = input()
first = input()
target = input()

cnt = 0
min_cnt = 0
for s1, s2 in zip(first, target):
    if s1 == s2:
        min_cnt += 1 if cnt else 0
        cnt = 0
        continue
    cnt += 1

answer = min_cnt
print(answer)