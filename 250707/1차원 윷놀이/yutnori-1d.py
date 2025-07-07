def play():
    global nums, poses, turns
    for i in range(N):
        poses[nums[i]] += turns[i]

    cnt = 0
    for p in poses:
        if p >= M - 1:
           cnt += 1
    
    poses = [0] * (N + 1)

    return cnt 


def select_nums(cnt):
    global nums, N, answer
    if cnt == N:
        answer = max(answer, play())
        return
        
    for i in range(1, K + 1):
        nums.append(i)
        select_nums(cnt + 1)
        nums.pop()


N, M, K = map(int, input().split())
turns = list(map(int, input().split()))
nums, poses, answer = [], [0] * (N + 1), 0

select_nums(0)

print(answer)