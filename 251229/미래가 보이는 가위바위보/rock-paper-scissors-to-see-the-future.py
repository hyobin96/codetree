# 묵으로 이긴 것
# 찌로 이긴 것
# 빠로 이긴 것
# 3개의 배열

# 묵 찌 -> 찌로 이긴 건 묵으로는 이길 수 없음
# 묵 빠 -> 빠로 이긴 건 묵으로는 비김
# 다른 것도 마찬가지

import sys

input = sys.stdin.readline

n = int(input())

queries = [input() for _ in range(n)]

def is_win(q1, q2):
    if q1 == 'H' and q2 == 'S':
        return True
    if q1 == 'S' and q2 == 'P':
        return True
    if q1 == 'P' and q2 == 'H':
        return True

    return False

h_wins, s_wins, p_wins = [0] * (n + 1), [0] * (n + 1), [0] * (n + 1)

for i, q in enumerate(queries):
    h_wins[i + 1] = h_wins[i] + int(is_win('H', q))
    s_wins[i + 1] = s_wins[i] + int(is_win('S', q))
    p_wins[i + 1] = p_wins[i] + int(is_win('P', q))
