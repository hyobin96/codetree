n = int(input())

arr = list(map(int, input().split()))

res = arr[0]
def _max(arr, i, res):
    if i == len(arr):
        return res
    if arr[i] > res:
        res = arr[i]
    return _max(arr, i+1, res)

print(_max(arr, 0, res))