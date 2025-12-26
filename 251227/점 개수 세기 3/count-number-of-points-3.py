n, q = map(int, input().split())

# n 개의 점의 위치 입력받고 오름차순 정렬
points = list(map(int, input().split()))
points.sort()

# 1부터 시작해서 정렬한 리스트에 가장 앞의 숫자부터 매핑, dict에 (기존 값, 매핑한 값) 으로 기록
hash_set = dict()
mapping_num = 1

for p in points:
    hash_set[p] = mapping_num
    mapping_num += 1

# 점의 개수는 dict(b) - dict(a) + 1 개
for _ in range(q):
    a, b = map(int, input().split())
    print(hash_set[b] - hash_set[a] + 1)