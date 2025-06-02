n, m = map(int, input().split())
arr = [0] + list(map(int, input().split()))

def sum_(a1, a2):
    global arr
    return sum(arr[a1:a2+1])

for _ in range(m):
    a1, a2 = map(int, input().split())
    print(sum_(a1, a2))