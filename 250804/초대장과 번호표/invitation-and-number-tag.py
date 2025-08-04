N, G = map(int, input().split())

group = []
group_size = []

for _ in range(G):
    nums = list(map(int, input().split()))
    group_size.append(nums[0])
    group.append(set(nums[1:]))

# Please write your code here.

answer = 1
subs = {1}
while subs:
    next_subs = set()
    for g in group:
        g -= subs
        if len(g) == 1:
            next_subs |= g

    subs = next_subs
    answer += len(subs)

print(answer)