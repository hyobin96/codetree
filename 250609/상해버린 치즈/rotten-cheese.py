n, m, d, s = map(int, input().split())
d_arr = [tuple(map(int, input().split())) for _ in range(d)]
s_arr = [tuple(map(int, input().split())) for _ in range(s)]

m_arr = [0] * (m+1)
n_arr = [0] * (n+1)

for n2, m2, t2 in d_arr:
    is_sang = True
    for n1, t1 in s_arr:
        if n1 == n2 and t1 > t2:
            is_sang = False
    if is_sang:
        m_arr[m2] = 1

for n1, m1, _ in d_arr:
    if m_arr[m1] == 1:
        n_arr[n1] = 1

print(sum(n_arr))