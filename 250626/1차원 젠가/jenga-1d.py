N = int(input())

arr = [int(input()) for _ in range(N)]

s1, e1 = map(int, input().split())
s2, e2 = map(int, input().split())
s1, e1, s2, e2 = map(lambda x: x - 1, (s1, e1, s2, e2))

def subtract(s, e):
    global arr
    temp_arr = []

    for i in range(len(arr)):
        if s <= i <= e:
            continue

        temp_arr.append(arr[i])

    arr = temp_arr[0:]


subtract(s1, e1)
subtract(s2, e2)

print(len(arr))
for i in range(len(arr)):
    print(arr[i])