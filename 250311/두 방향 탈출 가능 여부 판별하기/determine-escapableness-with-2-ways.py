import sys
sys.setrecursionlimit(10000) 

# N x M에서 좌측 상단에서 출발하여 우측 하단까지 뱀에 물리지 않고 탈출
# 아래 or 오른쪽으로 이동
# 탈출을 할 수 있는지 여부 판단

N, M = map(int, input().split())

graph = [list(map(int, input().split())) for _ in range(N)]

# 하, 우
d = [(1, 0), (0, 1)]

visited = [(0, 0)]

res = 0
def dfs(ci, cj):
    global d, N, M, res
    if (ci, cj) == (N-1, M-1):
        res = 1
        return 

    for di, dj in d:
        ni, nj = ci + di, cj + dj
        if 0 <= ni < N and 0 <= nj < N and (ni, nj) not in visited\
            and graph[ni][nj] != 0:
            visited.append((ni, nj))
            dfs(ni, nj)
dfs(0, 0)

print(res)
