N = int(input())
H_arr = [int(input()) for _ in range(N)]
diff = 17

def get_cost(min_H, max_H):
    cost = 0
    for e in H_arr:
        if min_H > e:
            cost += (min_H - e) ** 2
        elif max_H < e:
            cost += (e - max_H) ** 2
        
    return cost

min_cost = 2000000000
for min_H in range(max(H_arr)):
    cost = get_cost(min_H, min_H + diff)
    
    min_cost = min(min_cost, cost)

print(min_cost)