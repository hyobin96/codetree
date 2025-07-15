N = int(input())

def fibo():
    fibo = [-1] * (N + 1)
    fibo[1], fibo[2] = 1, 1
    for i in range(3, N + 1):
        fibo[i] = fibo[i - 1] + fibo[i - 2]
    print(fibo[N])

fibo()
