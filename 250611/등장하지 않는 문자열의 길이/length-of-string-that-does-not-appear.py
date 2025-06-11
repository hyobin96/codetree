import sys

N = int(input())
S = input()

_min = N
for length in range(1, N):
    is_one = True
    for i in range(N):
        s = S[i:i+length]
        for j in range(i+length, N):
            if s == S[j:j+length]:
                is_one = False
                break
    if is_one:
        print(length)
        sys.exit()
print(_min)

