def heapfiy(arr, i, n):
    largest = i
    left = i * 2
    right = left + 1

    if left <= n and arr[left] > arr[largest]:
        largest = left

    if right <= n and arr[right] > arr[largest]:
        largest = right

    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapfiy(arr, largest, n)
    

def heap_sort(arr, n):
    for i in range(n // 2, 0, -1):
        heapfiy(arr, i, n)

    for i in range(n, 1, -1):
        arr[1], arr[i] = arr[i], arr[1]
        heapfiy(arr, 1, i - 1)

n = int(input())
arr = [0] + list(map(int, input().split()))
heap_sort(arr, n)

print(*arr[1:])