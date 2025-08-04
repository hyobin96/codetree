N, G = map(int, input().split())

group = []
group_size = []

for _ in range(G):
    nums = list(map(int, input().split()))
    group_size.append(nums[0])
    group.append(nums[1:])

# Please write your code here.

# d = dict()

# for i in range(G):
#     if group_size[i] in d:
#         d[group_size[i]].append(group[i])
#     else:
#         d[group_size[i]] = [group[i]]

for g in group:
    g.sort()
group.sort(lambda x: (len(x), x))

answers = {1}
for _ in range(int(G ** 0.5) + 1):
    for g in group:
        s = set(g)
        sub = s - answers
        if len(sub) == 1:
            answers |= sub

print(len(answers))