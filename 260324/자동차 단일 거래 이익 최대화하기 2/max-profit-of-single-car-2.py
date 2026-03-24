n = int(input())
price = list(map(int, input().split()))

# Please write your code here.
prev_price = 100_000
max_profit = 0
for p in price:
    max_profit = max(max_profit, p - prev_price)
    prev_price = min(prev_price, p)

answer = max_profit
print(answer)    