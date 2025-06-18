N = int(input())
arr = list(map(int, input().split()))

arr.sort()

mins = []
for i in range(N):
    mins.append(arr[N + i] - arr[i])

print(min(mins))