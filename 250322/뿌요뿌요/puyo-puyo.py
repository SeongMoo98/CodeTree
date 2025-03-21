# N x N 격자

# 상하좌우, 같은 숫자로 이루어져 있는 경우 하나의 블럭
# 블럭을 이루고 있는 칸의 수가 4개 이상인 경우 해당 블럭 터짐

# 초기 상태가 주어졌을 때 터지게 되는 블럭의 수와 최대 블럭의 크기

N = int(input())

grid = [list(map(int, input().split())) for _ in range(N)]

d = [(-1, 0), (1, 0), (0, -1), (0, 1)]

visited = [[False] * N for _ in range(N)]
count, max_size = 0, 0

def dfs(grid, visited, curr, same_village):
    ci, cj = curr

    for di, dj in d:
        ni, nj = ci + di, cj + dj
        if 0 <= ni < N and 0 <= nj < N and visited[ni][nj] != True and grid[ci][cj] == grid[ni][nj]:
            visited[ni][nj] = True
            same_village.append((ni, nj))
            same_village = dfs(grid, visited, (ni, nj), same_village)

    return same_village


for i in range(N):
    for j in range(N):
        if visited[i][j] == False:
            visited[i][j] = True
            same_village = dfs(grid, visited, (i, j), [(i, j)])
            if len(same_village) >= 4:
                count += 1
            max_size = max(max_size, len(same_village))
        
print(count, max_size)



