N, K = map(int, input().split())
num_list = list(map(int, input().split()))

MAX_NUM = max(num_list)
MIN_NUM = min(num_list)

def get_cost(low, high):
    
    cost = 0
    for num in num_list:
        if num < low:
            cost += low - num
        
        elif num > high:
            cost += num - high

    return cost

min_cost = 2000000000
for low in range(MIN_NUM, MAX_NUM + 1):
    min_cost = min(min_cost, get_cost(low, low + K))

print(min_cost)