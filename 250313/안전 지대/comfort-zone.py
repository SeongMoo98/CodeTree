import sys
sys.setrecursionlimit(100000)
# N x M 격자
# 각 집의 높이는 1이상 100이하의 정수

# 비가 K만큼 온다면, 높이가 K 이하인 집들은 전부 물에 잠김
# ==> 각 K에 따라 안전 영역의 개수가 어떻게 달라지는지 확인하고자 않다
# 안전 영역 : 잠기지 않은 집들로 이루어져 있고, 서로 인접해 있는 경우 동일한 안전영역에 있는 것으로 간주

# 안전 영역의 수가 최대가 될 때 K과 그때의 안전 영역의 수를 구하여라

N, M = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(N)]

MAX_K = max([max(li) for li in matrix])

# 상, 하, 좌, 우
d = [(-1, 0), (1, 0), (0, -1), (0, 1)]


# (안전 영역의 수, k)
safety = []

def dfs(curr, k):
    ci, cj = curr[0], curr[1]
    
    for di, dj in d:
        ni, nj = ci + di, cj + dj
        if 0 <= ni < N and 0 <= nj < M and (ni, nj) not in visited and matrix[ni][nj] > k:
            visited.append((ni, nj))
            dfs((ni, nj), k)


# 최대 높이 -1 만큼 가능
for k in range(1, MAX_K):
    count = 0
    visited = []
    for i in range(N):
        for j in range(M):
            if (i, j) not in visited and matrix[i][j] > k:
                visited.append((i, j))
                dfs((i, j), k)
                count += 1
    if count != 0:
        safety.append((count, k))


safety.sort(key = lambda x:(-x[0], x[1]))

print(safety[0][0], safety[0][1])    
