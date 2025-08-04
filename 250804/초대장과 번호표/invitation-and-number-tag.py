N, G = map(int, input().split())

group = []
group_size = []

for _ in range(G):
    nums = list(map(int, input().split()))
    group_size.append(nums[0])
    group.append(nums[1:])

# Please write your code here.

for g in group:
    g.sort()
group.sort(lambda x: (len(x), x))

answers = {1}
while True:
    size = len(answers)
    for g in group:
        s = set(g)
        sub = s - answers
        if len(sub) == 1:
            answers |= sub

    if size == len(answers):
        break

print(len(answers))