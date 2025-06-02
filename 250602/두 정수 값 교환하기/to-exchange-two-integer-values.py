n, m = map(int, input().split())

def print_swap(a, b):
    a, b = b, a
    print(a, b)
print_swap(n, m)