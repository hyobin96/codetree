a, o, c = input().split()
a = int(a)
c = int(c)

def add(a, c):
    return a + c
def subtract(a, c):
    return a - c
def multiply(a, c):
    return a * c
def divide(a, c):
    return a // c

if o == '+':
    print(f'{a} {o} {c} = {add(a, c)}')
elif o == '-':
    print(f'{a} {o} {c} = {subtract(a, c)}')
elif o == '*':
    print(f'{a} {o} {c} = {multiply(a, c)}')
elif o == '/':
    print(f'{a} {o} {c} = {divide(a, c)}')
else:
    print('False')