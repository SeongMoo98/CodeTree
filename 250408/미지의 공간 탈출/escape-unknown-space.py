'''
미지의 공간 탈출

N x N 격자, 타임머신을 타고 공간을 탈출
N x N 격자 어딘가에는 한변의 길이가 M인 정육면체 형태의 시간의 벽이 세워져 있다

1. 타임머신의 스캔 기능
    (1) 미지의 공간 평면도 : 위에서 내려다본 전체 맵
    (2) 시간의 벽의 단면도 : 시간의 벽의 윗면과 동서남북 네 면의 단면도

    평면도와 단면도는 빈 공간(0)과 장애물(1)로 구성(타임머신을 통해 빈공간만 이동 가능)

2. 타임머신
    시간의 벽 윗면 단면도
    시간의 벽의 윗면 단면도에서 타임머신 위치 2가 추가로 표시

    미지의 공간 평면도
    시간의 벽의 위치 3과 탈출구 4가 표시

    탈출구는 시간의 벽 외부에 있는 미지의 공간 바닥에 위치

    시간의 벽과 맞닿은 미지의공간의 바닥은 장애물로 둘러쌓여있지만, 단 한칸만 빈공간
    ==> 시간의 벽 -> 미지의 공간으로 이어질 수 있는 단 하나의 출구

3. 시간 이상 현상
    F 개의 시간 이상 현상
    바닥의 빈 공간 (r, c)에서 시작하여 매 v의 배수 턴마다 방향 d로 한칸씩 확산
    확산한 이후에도 기존 위치의 시간 이상 현상은 사라지지 않는다
    빈공간으로 확산, 더이상 확산할 수 없으면 멈춤
    모든 이상현상은 독립적이며, 동시에 확산
    동 0, 서 1, 남 1 북 3

4. 타임머신 이동
    매 턴 마다 상하좌우로 한 칸씩 이동
    장애물과 시간 이상 현상을 피해 탈출구까지 도달해야 한다

이때, 타임머신이 시작점에서 탈출구까지 이동하는데 필요한 최소 시간(턴 수)를 출력
만약, 탈출할 수 없다면 -1출력
시간 이상 현상이 확산된 후 타임머신이 이동하기 때문에, 시간 이동 현상이 확산되는 곳으로 이동할 수 없음을 유의

미지의 공간 크기 N, 시간의 벽 크기 M, 시간 이상 현상 개수 F
5 <= N <= 20, 2 <= M <= 10, 1 <= F <= 10

시간 이상 현상
(r, c, d, v)
r, c : 0부터 주어진다
d : 우 0, 좌 1, 하 1, 상 3
v : 확산 상수(1 <= v <= 1000)
'''
from collections import deque
from filecmp import dircmp

# 미지의 공간 크기, 시간의 벽 크기, 시간 이상 현상 개수
N, M, F = map(int, input().split())

# 0(빈칸), 1(벽), 3(시간의 벽)
space_matrix = [list(map(int, input().split())) for _ in range(N)]

#   x N x
#   W U E
#   x S x
# 동, 서, 남, 북, 윗면의 단면도
# 전부 벽 
timewall_matrix = [[1] * (3 * M) for _ in range(3 * M)]

directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]


def make_timewall_matrix():
    east = [list(map(int, input().split())) for _ in range(M)]
    west = [list(map(int, input().split())) for _ in range(M)]
    south = [list(map(int, input().split())) for _ in range(M)]
    north = [list(map(int, input().split())) for _ in range(M)]
    up = [list(map(int, input().split())) for _ in range(M)]

    # 서 : 1바퀴, 북 : 2바퀴, 동 : 3바퀴
    for _ in range(1):
        west = list(map(list, zip(*west[::-1])))
    for i in range(M):
        for j in range(M):
            timewall_matrix[M + i][j] = west[i][j]

    for _ in range(2):
        north = list(map(list, zip(*north[::-1])))
    for i in range(M):
        for j in range(M):
            timewall_matrix[i][M + j] = north[i][j]

    for _ in range(3):
        east = list(map(list, zip(*east[::-1])))

    for i in range(M):
        for j in range(M):
            timewall_matrix[M + i][2 * M + j] = east[i][j]

    for i in range(M):
        for j in range(M):
            timewall_matrix[2 * M + i][M + j] = south[i][j]

    for i in range(M):
        for j in range(M):
            timewall_matrix[M + i][M + j] = up[i][j]


make_timewall_matrix()

abnormal = []
for _ in range(F):
    # (r, c), d(동 0, 서 1 남 2 북 3)
    r, c, d, v = map(int, input().split())
    abnormal.append((r, c, d, v))
    space_matrix[r][c] = -1


def find_exit():
    ei, ej, wi, wj, exit_i, exit_j = -1, -1, -1, -1, -1, -1
    for i in range(N):
        for j in range(N):
            if space_matrix[i][j] == 4:
                ei, ej = i, j
            if space_matrix[i][j] == 3 and (wi, wj) == (-1, -1):
                wi, wj = i, j

            if space_matrix[i][j] == 3:
                for di, dj in [(-1, 0), (1, 0), (0, 1), (0, -1)]:
                    ni, nj = i + di, j + dj
                    if 0 <= ni < N and 0 <= nj < N and space_matrix[ni][nj] == 0:
                        exit_i, exit_j = ni, nj
                        return ei, ej, wi, wj, exit_i, exit_j

    # 시간 이상 현상이 출구를 막아버림
    return -1, -1, -1, -1, -1, -1

def find_time_machine():
    # 타임머신 좌표 찾기
    for i in range(3 * M):
        for j in range(3 * M):
            if timewall_matrix[i][j] == 2:
                return i, j

def exit_time_wall(wi, wj, exit_i, exit_j):
    # [1] 시간의 벽 내에서 최단거리 구하기
    # 이는 항상 동일
    # 만약 출구 못찾으면 그냥 바로 종료

    # (wi, wj) : space matrix에서의 벽 좌 상단
    # (ei, ej) : space_matrix에서의 출구 좌표 ==> 위치 변환 필요

    def is_range(x, y):
        return 0 <= x < 3 * M and 0 <= y < 3 * M
    # 동 0, 서 1, 남 2, 북 3
    def move_to_wall(ni, nj, d):
        # 북 - >서
        if 0 <= ni < M and nj == M - 1 and d == 1:
            ni, nj = M, ni
        # 서 -> 북
        elif ni == M - 1 and 0 <= nj < M and d == 2:
            ni, nj = nj, M

        # 북 -> 동
        elif 0 <= ni < M and nj == 2 * M and d == 0:
            ni, nj = M, 3 * M - 1 - ni
        # 동 -> 북
        elif ni == M - 1 and 2 * M <= nj < 3 * M and d == 3:
            ni, nj = 3 * M - 1 - nj, 2 * M - 1

        # 서 -> 남
        elif ni == 2 * M and 0 <= nj < M and d == 2:
            ni, nj = 3 * M - 1 - nj, M
        # 남 -> 서
        elif 2 * M <= ni < 3 * M and nj == M - 1 and d == 1:
            ni, nj = 2 * M - 1, 3 * M - 1 - ni

        # 남 -> 동
        elif 2 * M <= ni < 3 * M and nj == 2 * M and d == 0:
            ni, nj = 2 * M - 1, ni
        # 동 -> 남
        elif ni == 2 * M and 2 * M <= nj < 3 * M and d == 2:
            ni, nj = nj, 2 * M - 1
            
        return ni, nj

    si, sj = find_time_machine()

    # (ei, ej)가 북쪽에
    if exit_i < wi:
        exit_i, exit_j = -1, M + (exit_j - wj)
    # (ei, ej)가 서쪽에
    elif exit_j < wj:
        exit_i, exit_j = M + (exit_i - wi), -1
    # (ei, ej)가 동쪽에
    elif exit_j > wj + M -1:
        exit_i, exit_j = M + (exit_i - wi) , 3 * M
    # (ei, ej)가 남쪽에
    elif exit_i > wi + M - 1:
        exit_i, exit_j = 3 * M, M + (exit_j - wj)

    q = deque()
    visited = [[(0, 0)] * (3 * M) for _ in range(3 * M)]

    q.append((si, sj))
    visited[si][sj] = (si, sj)
    path = []
    while q:
        ci, cj = q.popleft()
        for d in range(4):
            ni, nj = ci + directions[d][0], cj + directions[d][1]
            
            # 벽면 이동 가능하면 이동
            ni, nj = move_to_wall(ni, nj, d)

            # 격자 내 빈칸이면 그냥 갈 수 있다.
            if is_range(ni, nj) and visited[ni][nj] == (0, 0) and timewall_matrix[ni][nj] == 0:
                q.append((ni, nj))
                visited[ni][nj] = (ci, cj)

            # 격자 밖 and 출구
            if not is_range(ni, nj) and (ni, nj) == (exit_i, exit_j):
                path = [(ci, cj)]
                while True:
                    if (ci, cj) == (si, sj):
                        return len(path)
                    ni, nj = visited[ci][cj]
                    path.append((ni, nj))
                    ci, cj = ni, nj

            # 다른 면으로 이동하는 코드
            # 격자 내, 다른 면, 미방문
    return 0

def spread(time):
    global abnormal
    temp_ab = [x[:] for x in abnormal]
    for i in range(len(abnormal)):
        r, c, d, v = abnormal[i]
        if time % v == 0:
            nr, nc = r + directions[d][0], c + directions[d][1]
            if 0 <= nr < N and 0 <= nc < N and space_matrix[nr][nc] == 0:
                space_matrix[nr][nc] = -1
                temp_ab.append((nr, nc, d, v))
    abnormal = temp_ab

# 탈출구,시간의 벽 좌상단, 시간의 벽 출구 찾기
ei, ej, wi, wj, exit_i, exit_j = find_exit()
if (ei, ej) == (-1, -1):
    print(-1)
else:
    curr_time = exit_time_wall(wi, wj, exit_i, exit_j)


    if curr_time == 0:
        print(-1)
    else:
        # 현재 t 시간이 지난 상황이기 때문에 확산을 다 시켜놓기
        for t in range(1, curr_time+1):
            spread(t)
        # curr_time += 1

        # [1] 시간의 벽 출구 -> 탈출구 한칸 이동(최단거리 찾고) -> 확산을 계속 반복
        # (exit_i, exit_j) => (ei, ej)로 가는 최단 거리
        q = deque()
        visited = [[False] * N for _ in range(N)]

        q.append((exit_i, exit_j))
        visited[exit_i][exit_j] = True
        flag = False

        while q:
            nq = deque()

            # 동일 반경(즉, 같은 시간내에서 갈 수 있는 곳)
            for ci, cj in q:
                if (ci, cj) == (ei, ej):
                    flag = True
                    break

                for di, dj in directions:
                    ni, nj = ci + di, cj + dj
                    if 0 <= ni < N and 0 <= nj < N and visited[ni][nj] == False and (space_matrix[ni][nj] == 0 or space_matrix[ni][nj] == 4):
                        nq.append((ni, nj))
                        visited[ni][nj] = True
            q = nq

            # 시간 이상
            spread(curr_time)
            curr_time += 1

        if flag:
            print(curr_time)
        else:
            print(-1)


        






