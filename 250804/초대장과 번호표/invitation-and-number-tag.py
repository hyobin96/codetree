N, G = map(int, input().split())

group = [set(list(map(int, input().split()))[1:]) for _ in range(G)]

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