def merge_sort(arr, low, high):
    if low < high:
        mid = (low + high) // 2
        merge_sort(arr, low, mid)
        merge_sort(arr, mid+1, high)
        merge(arr, low, mid, high)

def merge(arr, low, mid, high):
    sorted_arr = []

    i = low
    j = mid + 1
    k = low

    while i <= mid and j <= high:
        if arr[i] <= arr[j]:
            sorted_arr.append(arr[i])
            i += 1
        else:
            sorted_arr.append(arr[j])
            j += 1

    while i <= mid:
        sorted_arr.append(arr[i])
        i += 1

    while j <= high:
        sorted_arr.append(arr[j])
        j += 1

    l = 0
    while k <= high:
        arr[k] = sorted_arr[l]
        k += 1
        l += 1


n = int(input())
arr = list(map(int, input().split()))

merge_sort(arr, 0, n-1)
print(*arr)
