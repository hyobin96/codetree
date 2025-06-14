N, M, p = map(int, input().split())
m_arr = []
person_arr = [1] * N

for _ in range(M):
    c, u = input().split()
    c = ord(c) - ord('A') 
    u = int(u)
    m_arr.append((c, u))

for i in range(p - 1, M):
    c, u = m_arr[i]
    person_arr[c] = 0

if m_arr[p - 1][1] == m_arr[p - 2][1]:
    person_arr[m_arr[p - 2][0]] = 0

if m_arr[p - 1][1] != 0:
    for i, v in enumerate(person_arr):
        if v == 1:
            print(chr(i + ord('A')), end = ' ')

