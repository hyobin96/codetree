N, K = map(int, input().split())
arr = list(map(int, input().split()))

def is_possible(max_value):
    pos_elems = []
    for i, v in enumerate(arr):
        if v <= max_value:
            pos_elems.append(i)
    
    for i in range(len(pos_elems) - 1):
        dist = pos_elems[i+1] - pos_elems[i]
        if dist > K:
            return False
    
    return True

min_value = 0
for max_value in range(max(arr), max(arr[0], arr[-1]) - 1, -1):
    if is_possible(max_value):
        min_value = max_value
    else:
        break

print(min_value)