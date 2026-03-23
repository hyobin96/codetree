n, k = map(int, input().split(" "))
coins = [int(input()) for _ in range(n)]

# Please write your code here.
coins.sort(reverse = True)

cnt = 0
for coin in coins:
    q, k = divmod(k, coin)
    cnt += q

print(cnt) 
