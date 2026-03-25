N = int(input())
begin = list(input())
target = list(input())

# Please write your code here.
cnt = 0
for i in range(N):
    if begin[i] != target[i]:
        cnt += 1
        for j in range(i, min(i + 4, N)):
            if begin[j] != target[j]:
                begin[j] = target[j]
                continue
            break

print(cnt)