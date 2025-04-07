'''
마법의 숲 탐색

정령들이 R행 C열의 격자 형태로 이루어진 마법의 숲을 탐색(자장 위를 1행, 가장 아래는 R행)
숲의 동쪽, 서쪽, 남쪽은 막혀있으며, 정령들은 북쪽을 통해서만 들어올 수 있다.

K명의 정령은 각자 골렘을 타고 숲을 탐색
골렘 : 십자 모양(중앙까지 포함해서 5칸), 중앙을 제외한 4칸 중 출구 존재
정령 : 어떤 방향에서든 골렘에 탑승 가능, 출구로만 나갈 수 있다.

i번째로 숲을 탐색하는 골렘은 숲의 가장 북쪽에서 시작해 골렘의 중앙이 c_i열이 되도록 하는 위치에서
내려오기 시작
초기 골렘의 출구는 d_i 방향에 위치

아래와 같은 우선순위로 더이상 움직이지 못할때까지 이동
1. 남쪽으로 한칸
2. 남쪽으로 못가면 서쪽 방향으로 회전하면서 한칸 아래(출구가 반시계방향 회전)
3. 서쪽 방향으로 못가면 동쪽 방향으로 회전하면서 한칸 아래(출구가 시계방향 회전)

골렘이 이동할 수 있는 가장 남쪽에 도달해 더이상 이동할 수 없으면, 정령은 골렘 내에서 상하좌우 이동 가능
만약, 골렘의 출구가 다른 골렘과 인접하고 있다면 해당 출구를 통해 이동 가능

정령은 갈 수 있는 모든 칸 중 가장 남쪽의 칸으로 이동하고 이동을 종료

만약, 골렘이 최대한 남쪽으로 이동했지만 골렘의 몸 일부가 여전히 숲을 벗어난 상태라면,
해당 골렘을 포함한 숲의 모든 골렘들은 숲을 빠져나간 뒤 다른 골렘부터 숲을 탐색
이 때 해당 정령의 행 번호는 답에 포함 x
==> 즉, 배열을 모두 비우고 다음 정령부터 탐색 시작

모든 정령의 최종 위치의 행번호의 합을 구하여라

격자 크기 R, C 정령의 수 K
5 <= R, C <= 70, 1 <= K <= 1000
'''
from collections import deque
N, M, K = map(int, input().split())

matrix = [[0] * M for _ in range(N+3)]

exit = set()
# 북, 동, 남, 서
d = [(-1, 0), (0, 1), (1, 0), (0, -1)]

# 다음 이동 확인하기 위한 함수
def is_range(ci, cj):
    return 0 <= ci < N+3 and 0 <= cj < M

def down(si, sj):
    # (si + 2, sj), (si + 1, sj - 1), (si + 1, sj + 1)
    if is_range(si+2, sj) and is_range(si+1, sj-1) and is_range(si+1, sj+1):
        return (matrix[si+2][sj] == 0) and (matrix[si+1][sj-1] == 0) and (matrix[si+1][sj+1] == 0)
    return False

def west(si, sj):
    # (si, sj-2), (si-1, sj-1), (si+1, sj-1), (si+1, sj-2), (si+2, sj-1)
    if is_range(si, sj-2) and is_range(si-1, sj-1) and is_range(si+1, sj-1) and is_range(si+1, sj-2) and is_range(si+2, sj-1):
        return (matrix[si][sj-2] == 0) and (matrix[si-1][sj-1] == 0) and (matrix[si+1][sj-1] == 0) and (matrix[si+1][sj-2] == 0) and (matrix[si+2][sj-1] == 0)
    return False

def east(si, sj):
    # (si, sj+2), (si-1, sj+1), (si+1, sj+1), (si+1, sj+2), (si+2, sj+1)
    if is_range(si, sj+2) and is_range(si-1, sj+1) and is_range(si+1, sj+1) and is_range(si+1, sj+2) and is_range(si+2, sj+1):
        return (matrix[si][sj+2] == 0) and (matrix[si-1][sj+1] == 0) and (matrix[si+1][sj+1] == 0) and (matrix[si+1][sj+2] == 0) and(matrix[si+2][sj+1] == 0)
    return False

def move(si, sj, ei, ej, d_i):
    # 정령 위치 : (si, sj)
    # 출구 위치 : (ei, ej)
    # 정령을 계속 이동 시켰다가 마지막에 출구 갱신 후 exit에 추가
    can_down, can_west, can_east = False, False, False
    while True:
        can_down = down(si, sj)
        if can_down:
            # 남쪽 이동
            si, sj = si + 1, sj
            ei, ej = ei + 1, ej
        else:
            can_west = west(si, sj)
            if can_west:
                # 서쪽 이동
                si, sj = si + 1, sj - 1
                d_i = (d_i - 1) % 4
                ei, ej = si + d[d_i][0], sj + d[d_i][1]
            else:
                can_east = east(si ,sj)
                if can_east:
                    si, sj = si + 1, sj + 1
                    d_i = (d_i + 1) % 4
                    ei, ej = si + d[d_i][0], sj + d[d_i][1]
                else:
                    # 위에서 걸려서 못내려 갔거나, 다 내려 갔거나
                    break

    return si, sj, ei, ej, d_i



def move_angle(si, sj):
    # 현재 위치에서 BFS
    # 1. 출구에서 다른 골렘과 접한다면 이동
    # 2. 현재 같은 골렘 내에서는 이동

    q = deque()
    visited = [[False] * M for _ in range(N+3)]

    q.append((si, sj))
    visited[si][sj] = True
    max_i = si

    while q:
        ci, cj = q.popleft()

        for di, dj in d:
            ni, nj = ci + di, cj + dj
            # 범위 내, 미방문
            if 3 <= ni < N+3 and 0 <= nj < M and visited[ni][nj] == False:
                # 현재 출구이면서 다른 골렘과 접함, 같은 골렘 내
                if ((ci, cj) in exit and matrix[ni][nj] > 0) or (matrix[ci][cj] == matrix[ni][nj]):
                    q.append((ni, nj))
                    visited[ni][nj] = True
                    max_i = max(max_i, ni)
    # 3칸이 추가됐고 0부터 시작하기 떄문에
    return max_i - 3 + 1

res = 0
# k번째 정령
for k in range(1, K+1):
    # 출발하는 열, 출구 방향
    # d_i : 북, 동, 남, 서(0 ~ 3)
    c_i, d_i = map(int, input().split())
    c_i -= 1

    # 초기 정령, 출구 좌표
    si, sj = 1, c_i
    ei, ej = si + d[d_i][0], sj + d[d_i][1]

    # [1] 골렘 이동
    si, sj, ei, ej, d_i = move(si, sj, ei, ej, d_i)

    # [2] 이동 불가면 Matrix 초기화(이동 후 정령의 위치가 1, 2, 3)
    # 이걸 하면 continue(현재 정령은 이동 x)
    if 1 <= si <= 3:
        matrix = [[0] * M for _ in range(N+3)]
        # 출구도 초기화
        exit = set()
        continue
    else:
        # 현재 골렘 Matrix 반영, Exit 추가
        matrix[si][sj] = k
        for di, dj in d:
            ni, nj = si + di, sj + dj
            matrix[ni][nj] = k
        exit.add((ei, ej))
    # [3] 정령 이동
    res += move_angle(si, sj)

print(res)