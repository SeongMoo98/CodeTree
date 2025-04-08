'''
또한, 시간을 처리하는 과정에서 시간 이상 현상이 먼저 일어난다는 조건을 깜빡하고 반대로 처리했다
애초에 3차원을 접근하는 법을 짜는데 오래 걸렸다..!
==> 조건, 하드코딩하는 것들은 시간을 들여서라도 한번에 꼼꼼하게  !!
'''

'''
문제 조건)
1. 미지의 공간 평면도(N x N) 0 : 빈공간, 1 : 장애물
2. 시간의 벽 단면도(동,서,남,북,윗면) M x M
3. F개의 시간 이상 현상 : (r, c) 시작, v의 배수 턴마다 방향 d로 확산

[입력]
방향 : 동(0), 서(1), 남(2), 북(3)
크기 : 5 <= N <= 20, 2 <= M <= min(N-2, 10)
이상현상 : 1 <= F <= 10
'''

'''
풀이 Idea)
1. 3차원 공간에서 목표 좌표(출구)까지 이동하는 bfs_3d
    평면간의 이동처리를 잘하면 가능하다(하드코딩)
2. 출구에서 탈출구까지 이동하는 bfs_2d
    시간 이상 현상을 벽처리 해놓으면 된다
    
[1] 3차원, 2차원의 시작, 종료 좌표 탐색
[2] bfs_3d(경로 없으면 -1)
    평면 간 이동이 중요하다
[3] bfs_2d(시간 이상 현상 처리)


평면 전개도
                        (2, 2) (2, 1) (2, 0)
                        (1, 2) (1, 1) (1, 0)
                        (0, 2) (0, 1) (0, 0)

(2, 0) (1, 0) (0, 0)    (0, 0) (0, 1) (0, 2)   (0, 2) (1, 2) (2, 2)
(2, 1) (1, 1) (0, 1)    (0, 0) (0, 1) (0, 2)   (0, 1) (1, 1) (2, 1)
(2, 3) (1, 2) (0, 2)    (0, 0) (0, 1) (0, 2)   (0, 0) (1, 0) (2, 2)

                        (0, 0) (0, 1) (0, 2)
                        (1, 0) (1, 1) (1, 2)
                        (2, 0) (2, 1) (2, 2)
'''



def find_3d_start():
    for i in range(M):
        for j in range(M):
            if arr_3d[4][i][j]==2:
                return 4,i,j

def find_2d_end():
    for i in range(N):
        for j in range(N):
            if arr[i][j]==4:
                arr[i][j]=0
                return i, j

def find_3d_base():
    for i in range(N):
        for j in range(N):
            if arr[i][j]==3:
                return i, j

def find_3d_end_2d_start():
    # 3차원의 시작 좌상단 좌표
    bi, bj = find_3d_base()
    ek_3d, ei_3d, ej_3d, si, sj = 0, 0, 0, 0, 0
    # 3차원 좌표에서 2차원 연결 좌표 찾기(출구)
    for i in range(bi, bi + M):
        for j in range(bj, bj + M):
            if arr[i][j] != 3:
                continue

            if arr[i][j + 1] == 0:  # 우측에 2차 시작점(3차원 우측으로 1차출구)
                return 0, M - 1, (M - 1) - (i - bi), i, j + 1  # ek(평면)=0, ei=M-1, ej=i, si=i, sj=j+1
            elif arr[i][j - 1] == 0:  # 좌측으로 1차출구!
                return 1, M - 1, i - bi, i, j - 1  # ek(평면)=1, ei=M-1, ej=i, si=i, sj=j+1
            elif arr[i + 1][j] == 0:  # 아래쪽으로 1차출구!
                return 2, M - 1, j - bj, i + 1, j  # ek(평면)=2, ei=M-1, ej=i, si=i, sj=j+1
            elif arr[i - 1][j] == 0:  # 위쪽으로 1차출구!
                return 3, M - 1, (M - 1) - (j - bj), i - 1, j  # ek(평면)=3, ei=M-1, ej=i, si=i, sj=j+1

    #         if arr[i][j+1] == 0:        # 우측에 출구
    #             # 북쪽, (M-1, j 역순), (i, j+1)
    #             ek_3d, ei_3d, ej_3d, si, sj = 0, M-1, (M-1)-(i-bi), i, j+1
    #         elif arr[i][j-1] == 0:      # 좌측에 출구
    #             ek_3d, ei_3d, ej_3d, si, sj = 1, M-1, i-bi, i, j-1
    #         elif arr[i+1][j] == 0:      # 아래쪽에 출구
    #             ek_3d, ei_3d, ej_3d, si, sj = 2, M-1, j-bj, i+1, j
    #         elif arr[i-1][j] == 0:      # 위쪽에 출구
    #             ek_3d, ei_3d, ej_3d, si, sj = 3, M-1, (M-1)-(j-bj), i-1, j
    #
    # return ek_3d, ei_3d, ej_3d, si, sj

from collections import deque
# 왼쪽, 오른쪽 평면 이동할 때의 look - up table
left_nxt = {0:2, 2:1, 1:3, 3:0}
right_nxt = {0:3, 2:0, 1:2, 3:1}
def bfs_3d(sk, si, sj, ek, ei, ej):
    q = deque()
    # 5개 평면에 대한 visited
    # 거리 기록
    visited = [[[0] * M for _ in range(M)] for _ in range(5)]

    q.append((sk, si, sj))
    visited[sk][si][sj] = 1

    while q:
        ck, ci, cj = q.popleft()

        if (ck, ci, cj) == (ek, ei, ej):
            return visited[ck][ci][cj]

        # 네 방향, 범위내 / 범위 밖 -> 다른 평면 이동 처리, 미방문
        for di, dj in [(-1, 0), (1, 0), (0, 1), (0, -1)]:
            ni, nj = ci + di, cj + dj

            # 범위 밖
            # ni < 0 : 위쪽 평면으로 이동
            # ck == 0 : nk, ni, nj = 4, (M-1) - cj, M-1
            # ck == 1 : nk, ni, nj = 4, cj, 0
            # ck == 2 : nk, ni, nj = 4, M - 1, cj
            # ck == 3 : nk, ni, nj = 4, 0, (M-1) - cj
            # ck == 4 : nk, ni, nj = 3, 0, (M-1) - cj
            if ni < 0:  # 위쪽 범위 이탈
                if ck == 0:
                    nk, ni, nj = 4, (M - 1) - cj, M - 1
                elif ck == 1:
                    nk, ni, nj = 4, cj, 0
                elif ck == 2:
                    nk, ni, nj = 4, M - 1, cj
                elif ck == 3:
                    nk, ni, nj = 4, 0, (M - 1) - cj
                elif ck == 4:
                    nk, ni, nj = 3, 0, (M - 1) - cj
            # ni >= M : 아래쪽 평면으로 이동
            # ck == 0, 1, 2, 3 : x
            # ck == 4 : nk, ni, nj = 2, 0, cj
            elif ni >= M:  # 아래쪽 범위이탈
                if ck == 4:
                    nk, ni, nj = 2, 0, cj
                else:
                    continue
            # nj < 0 : 왼쪽 평면으로 이동
            # ck == 0 : nk, ni, nj = 2, ci, M-1
            # ck == 1 : nk, ni, nj = 3, ci, M-1
            # ck == 2 : nk, ni, nj = 1, ci, M-1
            # ck == 3 : nk, ni, nj = 0, ci, M-1
            # ck == 4 : nk, ni, nj = 1, 0, (M-1) - ci
            elif nj < 0:  # 왼쪽 범위이탈
                if ck == 4:
                    nk, ni, nj = 1, 0, ci
                else:
                    # 위쪽 평면 빼고는 동일하기 때문에 Look-up table을 통해 간단히 구현
                    nk, ni, nj = left_nxt[ck], ci, M - 1
            # nj >= M : 오른쪽 평면으로 이동
            # ck == 0 : nk, ni, nj = 2, ci, 0
            # ck == 1 : nk, ni, nj = 3, ci, 0
            # ck == 2 : nk, ni, nj = 1, ci, 0
            # ck == 3 : nk, ni, nj = 0, ci, 0
            # ck == 4 : nk, ni, nj = 0, 0, (M-1) - ci
            elif nj >= M:  # 오른쪽 범위이탈
                if ck == 4:
                    nk, ni, nj = 0, 0, (M - 1) - ci
                else:
                    nk, ni, nj = right_nxt[ck], ci, 0
            else:  # 이탈아니면 같은 평면
                nk = ck

            ## 미방문, 조건 맞으면
            if visited[nk][ni][nj] == 0 and arr_3d[nk][ni][nj] == 0:
                q.append((nk,ni,nj))
                visited[nk][ni][nj] = visited[ck][ci][cj]+1
    # 경로 없을 때
    return -1
def bfs_2d(visited, dist, si, sj, ei, ej):
    q = deque()
    q.append((si,sj))
    visited[si][sj] = dist

    while q:
        ci, cj = q.popleft()
        if (ci, cj) == (ei, ej):
            return visited[ci][cj]

        for di, dj in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            ni, nj = ci + di, cj + dj
            if 0 <= ni < N and 0 <= nj < N and arr[ni][nj] == 0 and visited[ci][cj] + 1 < visited[ni][nj]:
                q.append((ni, nj))
                visited[ni][nj] = visited[ci][cj] + 1
    # 목적지를 찾을 수 없을 때
    return -1

N, M, F = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
# [0] : 동쪽, [1] : 서쪽, [2] : 남쪽, [3] : 북쪽, [4] : 위쪽 평면 단면도
arr_3d = [[list(map(int, input().split())) for _ in range(M)] for _ in range(5)]
wall = [list(map(int, input().split())) for _ in range(F)]

# [1] 주요 위치 찾기
# 3차원 평면 번호, 타임머신 위치(3차원 시작)
sk_3d, si_3d, sj_3d = find_3d_start()
# 탈출구(2차원 끝) 탐색
ei, ej = find_2d_end()
# 출구 탐색(3차원 평면번호, 평면에서의 좌표), 2차원에서 출구 좌표
ek_3d, ei_3d, ej_3d, si, sj = find_3d_end_2d_start()

# [2] 3차원 공간 탐색 : 시작 위치 -> 탈출 위치 거리 탐색(BFS 최단거리)
dist = bfs_3d(sk_3d, si_3d, sj_3d,ek_3d, ei_3d, ej_3d)

# 동 서 남 북
di=[ 0, 0, 1,-1]
dj=[ 1,-1, 0, 0]
if dist!=-1:
    # [3] 2차원 탐색 준비: 시간이상현상 처리해서 v에 시간표시: BFS확산시 그보다 작으면 통과하게표시
    v = [[401]*N for _ in range(N)]
    # 시간 이상 현상 처리
    # wv 단위로 wd방향으로 확산 표시(출구가 아닌 경우만)
    for wi, wj, wd, wv in wall:
        v[wi][wj] = 1
        for mul in range(1, N+1):
            wi,wj = wi+di[wd], wj+dj[wd]
            if 0<= wi <N and 0 <= wj <N and arr[wi][wj]==0 and (wi,wj) != (ei,ej):
                if v[wi][wj] > wv*mul:    # 더 큰 값 일때만 갱신(겹칠수있으니)
                    v[wi][wj] = wv*mul
            else:
                break

    # [4] 2차원 시작위치에서 BFS로 탈출구탐색(v에 적혀있는 값보다 작은 경우 지나감)
    dist = bfs_2d(v, dist, si, sj, ei, ej)


print(dist)

