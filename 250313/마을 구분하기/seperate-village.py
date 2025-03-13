import sys
sys.setrecursionlimit(100000) 
# N x N 크기 격자에 사람 or 벽이 존재
# 상하좌우의 인접한 영역에 있는 사람들은 같은 마을에 있는 것으로 간주

# 이 때, 총 마을의 개수와 같은 마을에 있는 사람의 수를 오름차순으로 정렬하여 출력

N = int(input())

# 사람 : 1, 벽 : 0
matrix = [list(map(int, input().split())) for _ in range(N)]

# 상, 하, 좌, 우
d = [(-1, 0), (1, 0), (0, -1), (0, 1)]

# 마을의 수
group = 0
# 각 마을의 사람 수
peoples = []

visited = [[False] * N for _ in range(N)]

# DFS에서 마지막 count값 return 하기
def dfs(curr):
    global people
    ci, cj = curr[0], curr[1]

    for di, dj in d:
        ni, nj = ci + di, cj + dj
        if 0 <= ni < N and 0 <= nj < N and matrix[ni][nj] == 1 and visited[ni][nj] == False:
            visited[ni][nj] = True
            dfs((ni, nj))
            people.append((ni, nj))



for i in range(N):
    for j in range(N):
        if matrix[i][j] == 1 and visited[i][j] == False:
            # 시작점 (i, j)
            visited[i][j] = True
            people = [(i, j)]
            dfs((i, j))
            peoples.append(len(people))
            group += 1

print(group)
[print(p) for p in sorted(peoples)]

