s, q = input().split()
q = int(q)
queries = [int(input()) for _ in range(q)]

for q in queries:
    if q == 1:
        s = s[1:] + s[0]
    elif q == 2:
        s = s[-1] + s[0:-1]
    else:
        s = s[::-1]
    print(s)