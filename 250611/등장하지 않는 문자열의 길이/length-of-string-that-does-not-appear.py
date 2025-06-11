import sys

N = int(input())
S = input()

for length in range(1, N+1):
    is_one = True
    for i in range(N):
        s = S[i:i+length]
        for j in range(N):
            if i == j:
                continue
            if s == S[j:j+length]:
                is_one = False
                break
    if is_one:
        print(length)
        sys.exit()

