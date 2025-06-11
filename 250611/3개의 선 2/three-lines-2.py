import sys

N = int(input())
arr = [tuple(map(int, input().split())) for _ in range(N)]

for i in range(11):        
    for j in range(i+1, 11):
        for k in range(j+1, 11):
            cnt = 0
            for l, e in enumerate(arr):
                for m in (i, j, k):
                    if m in e:
                        cnt += 1
                        break
            if cnt == N:
                print(1)
                sys.exit()                

