'''
고대 문명 유적 탐사

5 x 5 격자, 각 칸에 유물 조각 배치(1 ~ 7)

1. 탐사 진행
    3 x 3 격자 선택하여 항상 회전(90도, 180도, 270도)
    중심좌표를 기준으로 회전

    회전 목표
    가능한 회전의 방법 중
    (1) 유물의 1차 획득가치 최대화
    (2) 회전 각도가 가장 작은 방법
    (3) 중심좌표의 열, 행이 작은 방법

2. 유물 획득
    2-1. 1차 획득
        상하좌우, 같은 유물조각 3개이상
        유물의 가치는 모인 조각의 개수 -> 모인 조각들을 사라짐

        유적의 벽면
            1 ~ 7의 숫자 M개 -> 사라진 조각에 대한 정보
            (1) 열 번호가 작은 순
            (2) 행 번호가 큰 순
            이 때, 벽면의 숫자는 충분히 많아 적혀 조각의 수가 부족한 경우는 없다
            유적의 벽면에 써 있는 숫자를 사용한 이후에는 다시 사용할 수 없다

    2-2. 유물 연쇄 획득
        새로운 유물 조각이 생겨난 이후에도 조각들이 3개 이상 연결될 수 있다.
        1차 획득과 같은 방식으로 3개 이상의 조각들이 모여 사라짐
        이는 더 이상 3개 이상의 연결된 조각이 없을 때까지 진행

3. 탐사 반복
    탐사 진행 -> 유물획득(1차, 연쇄)의 과정을 1턴으로 하여, K턴 지냏ㅇ

각 턴마다 획득한 유물의 가치의 총합을 출력
아직 K번의 턴을 진행하지 못했지만, 탐사 진행 과정에서 어떠한 방법을 사용하더라도 유물을 획득하지 못하면 종료
이떄는 아무값도 출력 x


탐사 횟수 K, 유물 조각 개수 M
1 <= K <= 10, 10 <= M <= 300
'''
from collections import deque

from h5py.h5o import visit

# 격자 크기, 회전 격자 크기
N, L = 5, 3

# 탐사 횟수, 유물 조각 갯수
K, M = map(int, input().split())

arr = [list(map(int, input().split())) for _ in range(N)]
# 벽면 정보, 현재 idx
walls = list(map(int, input().split()))
curr_idx = 0


def bfs(si, sj, matrix, visited):
    # (si, sj)에서 출발하여 현재 arr값과 같은 곳

    q = deque()

    q.append((si, sj))
    visited[si][sj] = True

    path = [(si, sj)]
    while q:
        ci, cj = q.popleft()

        for di, dj in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            ni, nj = ci + di, cj + dj
            # 범위 내, 미방문, 동일 값
            if 0 <= ni < N and 0 <= nj < N and visited[ni][nj] == False and matrix[ci][cj] == matrix[ni][nj]:
                q.append((ni, nj))
                visited[ni][nj] = True
                path.append((ni, nj))

    return path

def rotate(si, sj, turn):
    # si, sj는 좌상단 좌표
    ret_arr = [x[:] for x in arr]

    for t in range(turn):
        for i in range(L):
            for j in range(L):
                ret_arr[si + i][sj + j] = arr[si + L - 1 - j][sj + i]
    return ret_arr


def search(matrix):
    # 유물 획득(탐사나 1차 획득이나 연쇄획득에서 동일하게 사용)
    total_count = 0
    visited = [[False] * N for _ in range(N)]
    points = []
    for i in range(N):
        for j in range(N):
            if visited[i][j]:
                continue
            path = bfs(i, j, matrix, visited)
            if len(path) >= 3:
                total_count += len(path)
                points.extend(path)
                for x, y in path:
                    visited[x][y] = True
    return total_count, points


def fill_arr():
    global arr, walls, curr_idx
    for j in range(N):
        for i in range(N - 1, -1, -1):
            if arr[i][j] == 0:
                arr[i][j] = walls[curr_idx]
                curr_idx += 1

for k in range(K):
    # [1] 탐사

    # 시작 좌표 (0, 0) ~ (2, 2) 까지 회전
    temp_list = []
    for si in range(N - L + 1):
        for sj in range(N - L + 1):
            # 1번(90도), 2번(180도), 3번(270도) 회전
            for turn in range(1, 4):
                temp_matrix = rotate(si, sj, turn)
                temp_cnt, _ = search(temp_matrix)
                # 개수, 회전 횟수, 중심 j, 중심 i
                temp_list.append((temp_cnt, turn, sj + 1, si + 1))
    # 유물 1차 획득이 많은, 회전 각도 작은, 중심 좌표의 열 j -> 행 i 이 작은
    temp_list.sort(key=lambda x: (-x[0], x[1], x[2], x[3]))
    cnt, angle, center_i, center_j = temp_list[0][0], temp_list[0][1], temp_list[0][3], temp_list[0][2]

    # 획득할 방법이 없을 때 종료
    if cnt == 0:
        break

    # [2] 회전
    # 중심좌표를 기준으로 center_i, center_j = (si + 1, sj +1)
    # [1]번의 기준에 맞게 arr 회전
    arr = rotate(center_i - 1, center_j - 1, angle)

    # [3] 유물 획득
    # 유물 획득 -> 유물 채우기 과정을 계속 반복
    turn_res = 0
    while True:
        # [3-1] 유물 획득
        cnt, points = search(arr)
        if cnt == 0:
            break
        turn_res += cnt
        # [3-2] arr 0처리
        for x, y in points:
            arr[x][y] = 0
        # [3-2] 유물 채우기
        fill_arr()
    print(turn_res, end=' ')


