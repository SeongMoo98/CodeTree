R, C = map(int, input().split())
grid = [list(input().split()) for _ in range(R)]

# Please write your code here.

# 점프 : 현재 색 != 점프한 색
# 적어도 한칸 이상 오른쪽 and 한칸 이상 아래쪽
# 시작, 도착 지점을 제외하고 점프하며 도달한 위치가 정확히 2곳(즉, 점프를 3번)
# 시작 -> 점프 1 -> 점프 2 -> 도착
# (0, 0) -> (i, j) -> (l, m) -> (R-1, C-1)

start, end = grid[0][0], grid[R-1][C-1]
count = 0
for i in range(1, R):
    for j in range(1, C):
        if start != grid[i][j]:
            curr = grid[i][j]
            for l in range(i+1, R-1):
                for m in range(j+1, C-1):
                    if curr != grid[l][m] and grid[l][m] != end:
                        count += 1 
print(count)
