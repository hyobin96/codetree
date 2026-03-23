N, M = map(int, input().split())
jewels = [tuple(map(int, input().split(" "))) for _ in range(N)]

# Please write your code here.
jewels.sort(key = lambda x: (- x[1] / x[0]))
max_value = 0
for w, v in jewels:
    if M >= w:
        max_value += v
        M -= w
        continue
    else:
        max_value += v * M / w
        break

max_value = round(max_value, 3)
print(f"{max_value:.3f}")