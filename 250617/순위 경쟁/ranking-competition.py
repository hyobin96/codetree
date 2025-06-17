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

    if A > B > C:
        return 3

    if A > C > B:
        return 4
    
    if B > A > C:
        return 5
    
    if B > C > A:
        return 6

    if C > A > B:
        return 7

    if C > B > A:
        return 8

    if B == C > A:
        return 9

value_arr = [0] * 3
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