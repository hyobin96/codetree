n, m, d, s = map(int, input().split())
d_arr = [tuple(map(int, input().split())) for _ in range(d)]
s_arr = [tuple(map(int, input().split())) for _ in range(s)]

m_arr = [0] * (m+1)
n_arr = [0] * (n+1)

count_arr = [[0] * s for _ in range(m+1)]
for i in range(1, m+1):
    for n2, m2, t2 in d_arr:
        for j, (n1, t1) in enumerate(s_arr):
            if n1 == n2 and i == m2 and t1 > t2:
                count_arr[i][j] = 1
                break
for i in range(1, m+1):
    if sum(count_arr[i]) == s:
        m_arr[i] = 1
for n1, m1, _ in d_arr:
    if m_arr[m1] == 1:
        n_arr[n1] = 1

print(sum(n_arr))