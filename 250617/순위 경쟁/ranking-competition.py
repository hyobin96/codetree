N = int(input())
arr = []
for _ in range(N):
    c, s = input().split()
    s = int(s)
    arr.append((c, s))

def bunru():
    if A == B == C:
        return 0
    
    if A == B > C:
        return 1
    
    if A == C > B:
        return 2

    if A > B and A > C:
        return 3
    
    if B > A and B > C:
        return 4

    if C > A and C > B:
        return 5

    if B == C > A:
        return 6

prev = 0
cnt = 0
A, B, C = 0, 0, 0
for c, s in arr:
    if c == 'A':
        A += s
    elif c == 'B':
        B += s
    else:
        C += s

    curr = bunru()
    if prev != curr:
        cnt += 1

    prev = curr

print(cnt)