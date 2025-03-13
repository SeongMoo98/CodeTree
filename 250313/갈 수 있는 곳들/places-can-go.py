# 0, 1로만 이루어진 N x N 격자
# K 개의 시작점으로부터 상 하 좌 우 인접한 곳으로만 이동하여 도달 가능한 칸의 수
# 이동 가능 : 0, 이동 불가 1

from collections import deque

N, K = map(int, input().split())

matrix = [list(map(int, input().split())) for _ in range(N)]
# 1 <= r_i, c_i <= N
starts = [list(map(int, input().split())) for _ in range(K)]

# 상, 하, 좌, 우
d = [(-1, 0), (1, 0), (0, -1), (0, 1)]

res = 0

visited = []
q = deque([])

for start in starts:
    si, sj = start[0] - 1, start[1] - 1
    if (si, sj) not in visited:
        visited.append((si, sj))
        q.append((si, sj))
        res += 1
        while q:
            ci, cj = q.popleft()

            for di, dj in d:
                ni, nj = ci + di, cj + dj
                if 0 <= ni < N and 0 <= nj < N and (ni, nj) not in visited and matrix[ni][nj] == 0:
                    visited.append((ni, nj))
                    q.append((ni, nj))
                    res += 1

print(res)