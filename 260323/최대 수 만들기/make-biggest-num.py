n = int(input())
arr = [input() for _ in range(n)]

# Please write your code here.
from functools import cmp_to_key

def compare(n1, n2):
    return int(n2 + n1) - int(n1 + n2)

arr.sort(key = cmp_to_key(compare))
print(''.join(arr))