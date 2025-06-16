N = int(input())
A, B = 0, 0
prev = 0
curr = 0

cnt = 0
for _ in range(N):
    c, score = input().split()
    score = int(score)

    if c == 'A':
        A += score
    else:
        B += score

    if A == B:
        curr = 0
    elif A < B:
        curr = 1
    else:
        curr = 2

    if prev != curr:
        cnt += 1
    
    prev = curr

print(cnt)