n, m = map(int, input().split())

A = [input() for _ in range(n)]
B = [input() for _ in range(n)]

# Please write your code here.

answer = 0
for i in range(m):
    for j in range(i + 1, m):
        for k in range(j + 1, m):
            s = set()
            is_possible = True
            for a in A:
                s.add(a[i] + a[j] + a[k])

            for b in B:
                if (b[i] + b[j] + b[k]) in s:
                    is_possible = False
                    break
            
            if is_possible:
                answer += 1

print(answer)