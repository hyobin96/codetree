n = int(input())

def print_1_N(n):
    if n == 0:
        return
    print_1_N(n - 1)
    print(n, end=' ')

def print_N_1(n):
    if n == 0:
        return
    print(n, end=' ')
    print_N_1(n - 1)

print_1_N(n)
print()
print_N_1(n)