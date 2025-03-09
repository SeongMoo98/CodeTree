n = int(input())
points = [tuple(map(int, input().split())) for _ in range(n)]
x = [p[0] for p in points]
y = [p[1] for p in points]

# Please write your code here.
# 1번 체크포인트 -> N번 체크포인트
# 1, N번 체크포인트 제외 체크포인트 건너뛰기
# 최소 거리(맨하탄)

min_dist = float('inf')


for skip_idx in range(1, n-1):
    ci, cj = 0, 0
    dist = 0    
    for j in range(1, n):
        ni, nj = x[j], y[j]
        if j == skip_idx:
            ci, cj = x[skip_idx-1], y[skip_idx-1]
            continue
        dist += abs(ni - ci) + abs(nj - cj)
        ci, cj = ni, nj
        
    min_dist = min(min_dist, dist)
print(min_dist)

