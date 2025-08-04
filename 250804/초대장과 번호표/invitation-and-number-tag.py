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

# for g in group:
#     g.sort()
# group.sort(lambda x: (len(x), x))

answers = {1}
for _ in range(G):
    for g in group:
        for _ in range(2):
            s = set(g)
            for n in g:
                if n in answers:
                    s.remove(n)
            if len(s) == 1:
                for n in s:
                    answers.add(n)

print(len(answers))
