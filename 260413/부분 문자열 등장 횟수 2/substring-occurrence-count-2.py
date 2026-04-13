target, query_count = input().rstrip().split()
query_count = int(query_count)
patterns = ['#' + input().rstrip() for _ in range(query_count)]

target = '#' + target
t_l = len(target)

for pattern in patterns:
    p_l = len(pattern)
    
    f = [0] * (p_l)
    f[0] = -1
    for i in range(1, p_l):
        j = f[i - 1]
        
        while j >= 0 and pattern[i] != pattern[j + 1]:
            j = f[j]

        f[i] = j + 1

    j = 0
    count = 0
    for i in range(1, t_l):

        while j >= 0 and pattern[j + 1] != target[i]:
            j = f[j]

        j += 1

        if j == p_l - 1:
            count += 1
            j = f[j]
    
    print(count)