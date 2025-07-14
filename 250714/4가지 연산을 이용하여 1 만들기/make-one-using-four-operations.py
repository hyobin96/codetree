from collections import deque

def in_range(curr):
    return 1 <= curr <= N + 2

def bfs(start):
    global visited
    q = deque()
    q.append(start)
    visited[start] = 1

    cnt = 0
    while q:
        q_size = len(q)
        for _ in range(q_size):
            curr = q.popleft()
            if curr == 1:
                return cnt
            
            if in_range(curr - 1) and not visited[curr - 1]:
                visited[curr - 1] = 1
                q.append(curr - 1)
            if in_range(curr + 1) and not visited[curr + 1]: 
                visited[curr + 1] = 1
                q.append(curr + 1)
            
            if curr % 2 == 0:
                next = curr // 2
                if not visited[next]:
                    visited[next] = 1
                    q.append(next)

            if curr % 3 == 0:
                next = curr // 3
                if not visited[next]:
                    visited[next]
                    q.append(next)

        cnt += 1
    
    return cnt

N = int(input())
visited = [0] * (N + 3)

answer = bfs(N)
print(answer)
        