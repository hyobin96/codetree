N, K = map(int, input().split())
nums = list(map(int, input().split()))
d = dict()
for n in nums:
    if n in d:
        d[n] += 1
    else:
        d[n] = 1

answer = 0
for i in range(N):
    for j in range(i + 1, N):
        target = K - nums[i] - nums[j]
        if target in d:
            cnt = d[target]
            if target == nums[i]:
                cnt -= 1
            if target == nums[j]:
                cnt -= 1
            answer += cnt

print(answer // 3)