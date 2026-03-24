n = int(input())

# Please write your code here.
cnt = 0
while n > 0:
    if (n - 5) % 2 == 0 or n % 5 == 0:
        n -= 5
        cnt += 1
    elif (n - 2) % 5 == 0 or n % 2 == 0:
        n -= 2
        cnt += 1
    else:
        cnt = -1
        n = 0

answer = cnt if n == 0 else -1
print(answer)
        