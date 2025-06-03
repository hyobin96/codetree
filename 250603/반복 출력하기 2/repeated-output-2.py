def print_hello(n):
    if n == 0:
        return
    print('HelloWorld')
    print_hello(n - 1)

n = int(input())
print_hello(n)