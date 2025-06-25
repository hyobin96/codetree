A = input()

def encoding(string):
    l = []
    cnt = 0
    for s in string:
        if cnt == 0:
            l.append(s)
            cnt += 1

        else:
            if s == l[-1]:
                cnt += 1
            else:
                l.append(str(cnt))
                l.append(s)
                cnt = 1

    if cnt != 0:
        l.append(str(cnt))

    return ''.join(l)

min_len = len(encoding(A))

string = A
for _ in range(len(A) - 1):
    string = string[-1] + string[ : -1]
    
    min_len = min(min_len, len(encoding(string)))

print(min_len)