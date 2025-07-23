from sortedcontainers import SortedDict

n = int(input())
words = [input() for _ in range(n)]

# Please write your code here.

sd = SortedDict()
for word in words:
    if word in sd:
        sd[word] += 1
    else:
        sd[word] = 1

for key, value in sd.items():
    print('{} {:.4f}'.format(key, value * 100 / n ))