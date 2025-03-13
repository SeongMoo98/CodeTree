# N x N 격자 ( 1이상 100 이하의 정수 )

# 특정 위치에서 시작하여 아래 조건을 만족하는 숫자의 위치를 찾아 상하좌우로 이동

# 1. 시작 위치의 수를 x라고 했을 때, 인접한 칸 중 x보다 작은 수 중 최대 값으로 이동
# 2. 이동할 수 있는 칸이 여러 개라면 행 번호 -> 열 번호가 작은 곳으로 이동
# 위 조건을 K번 반복한 이후의 위치를 구하여라

# K번을 반복하지 못했지만, 더 이상 새로 이동할 위치가 없다면 움직이는 것을 종료

from collections import deque

N, K = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(N)]
si, sj = map(int, input().split())
si, sj = si-1, sj-1

# 상, 하, 좌, 우
d = [(-1, 0), (1, 0), (0, -1), (0, 1)]


x = matrix[si][sj]

# 작은 수 중 큰 수, 행 작은, 열 작은
# 3개 원소를 가지는 tuple의 list

ei, ej = si, sj
flag = False

# 상, 하, 좌, 우 1칸이 아니라 다 움직일 수 있다.
for k in range(K):
    if flag:
        break

    visited = [(si, sj)]
    q = deque([(si, sj)])

    temp = []
    while q:
        ci, cj = q.popleft()
        
        for di, dj in d:
            ni, nj = ci+di, cj+dj
            if 0 <= ni < N and 0 <= nj < N and (ni, nj) not in visited and matrix[ni][nj] < x:
                temp.append((matrix[ni][nj], ni, nj))
                visited.append((ni, nj))
                q.append((ni, nj))

    if temp:
        temp.sort(key=lambda x:(-x[0], x[1], x[2]))
        si, sj = temp[0][1], temp[0][2]
        x = temp[0][0]
    else:
        flag = True

print(si + 1, sj + 1)

