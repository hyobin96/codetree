N = int(input())

s = set()
for _ in range(N):
    q, num = input().split()
    if q == 'find':
        if num in s:
            print('true')
        else:
            print('false')
    elif q == 'add':
        s.add(num)
    else:
        s.remove(num)