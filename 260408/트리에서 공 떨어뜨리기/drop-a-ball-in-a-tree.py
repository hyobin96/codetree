node_count = int(input())

tree = [0] * (node_count + 1)
for i in range(1, node_count + 1):
    l, r = map(int, input().split(" "))
    tree[i] = (l, r)

ball_count = int(input())
curr = 1
while True:
    l, r = tree[curr][0], tree[curr][1]
    if l == -1 == r:
        break
    elif l == -1:
        curr = r
    elif r == -1:
        curr = l
    else:
        if ball_count % 2 == 0:
            ball_count //= 2
            curr = r
        else:
            ball_count = ball_count // 2 + 1
            curr = l

print(curr)

    


