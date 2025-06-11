n = int(input())
arr = [tuple(map(int, input().split())) for _ in range(n)]

_max = 0
for i in range(1, 4):
    paper_cup = [0] * 4
    paper_cup[i] = 1
    score = 0
    for a, b, c in arr:
        paper_cup[a], paper_cup[b] = paper_cup[b], paper_cup[a]
        if paper_cup[c] == 1:
            score += 1
    _max = max(_max, score)
print(_max)