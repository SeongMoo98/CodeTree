from collections import deque
# N x M 좌측 상단에서 출발 -> 우측 하단 도착
# 상하좌우
# 뱀이 있는 칸 이동 X, 뱀에 물리지 않고 도착
# 뱀에 물리지 않고 탈출 가능한지 여부 확인

N, M = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(N)]

# 상, 하, 좌, 우
d = [(-1, 0), (1, 0), (0, -1), (0, 1)]

visited = [[0] * M for _ in range(N)]
visited[0][0] = 1
q = deque([(0, 0)])

while q:
    ci, cj = q.popleft()
    for di, dj in d:
        ni, nj = ci + di, cj + dj
        if 0 <= ni < N and 0 <= nj < M and visited[ni][nj] == 0 and graph[ni][nj] == 1:
            visited[ni][nj] = 1
            q.append((ni, nj))

print(visited[N-1][M-1])

