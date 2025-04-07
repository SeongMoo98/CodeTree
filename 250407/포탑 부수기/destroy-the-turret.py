# 
'''
포탑부수기

N x M 격자 위 모든 위치에 포탑 존재(NM개)

포탑
    공격력 존재(증가 감소 가능), 0이하가 되면 부서지며 더이상 공격 x
    최초에 공격력이 0인 포탑이 존재 가능

한턴(부서지지 않은 포탑이 1개가 되면 중지)
1. 공격자 선정
    부서지지 않은 포탑 중 가장 약한 포탑 선정 -> N + M 만큼 공격력 증가
    (1)가장 최근에 공격한, (2) 행 + 열 합이 큰, (3)열이 큰 포탑이 가장 약한 포탑
    모든 포탑은 시점 0에 모두 공격한 경험이 있다고 가정

2. 공격
    가장 약한 포탑이 가장 강한 포탑 공격
    (1) 가장 늦게 공격한 (2) 행 + 열이 작은, (3) 열이 작은 포탑이 가장 강한 포탑

    레이저 공격을 먼저 시도하고, 안되면 포탄 공격 실시
    2-1. 레이저 공격
        공격자의 위치에서 공격 대상 포탑까지의 최단 경로로 공격(존재하지 않으면 포탄 공격)
        경로의 길이가 같다면 (우, 하, 좌, 상)의 우선순위
        공격 대상 : 공격자의 공격력만큼 피해
        공격 경로의 포탑 : 공격자의 공격력 // 2만큼 피해

        상하좌우 이동, 부서진 포탑 지나지 못함, 가장 자리를 지나면 반대편으로 나옴

    2-2. 포탄 공격
    공격 대상 : 공격자의 공격력만큼 피래
    공격자 주위 8개의 포탑 : 공격자의 공격력 // 2만큼 피해(공격자는 피해 x)
    레이저 공격처럼 반대편 격자에도 영향을 준다

3. 포탑 부서짐
    공격을 받아 공격력이 0이하가 된 포탑은 부서짐

4. 포탑 정비
    부서지지 않은 포탑 중, 공격과 무관했던 포탑은 공격력 + 1(공격자 x, 공격 대상 x, 경로 or 주변 x)

전체 과정이 종료된 후에 남아있는 포탑 중 가장 강한 포탑의 공격력을 출력

격자 크기 N x M : 4 <= N, M <= 10
턴 K: 1 <= K <= 1000
'''
from collections import deque

N, M, K = map(int, input().split())

matrix = [list(map(int, input().split())) for _ in range(N)]

alive = 0
for i in range(N):
    for j in range(M):
        if matrix[i][j] > 0:
            alive += 1

# 현재 0번째 turn에 모두 공격했다고 가정
# 가장 최근에 공격한 turn 기록
attacked = [[0] * M for _ in range(N)]

def find_attacker(matrix, attacked):
    # 가장 약한 -> (가장 최근에 공격, i + j 큰, j 큰)
    min_value = float('inf')
    mi, mj = -1, -1
    for i in range(N):
        for j in range(M):
            if matrix[i][j] == 0:
                continue

            if min_value > matrix[i][j]:
                min_value = matrix[i][j]
                mi, mj = i, j
            elif min_value == matrix[i][j]:
                # 가장 최근에 공격(attack의 값이 큰)
                if attacked[mi][mj] < attacked[i][j]:
                    mi, mj = i, j
                elif attacked[mi][mj] == attacked[i][j]:
                    # 행 + 열의 합이 큰
                    if mi + mj < i + j:
                        mi, mj = i, j
                    elif mi + mj == i + j:
                        # 열의 값이 큰
                        if mj < j:
                            mi, mj = i, j
    return mi, mj


def find_target(matrix, attacked, si, sj):
    # 가장 강한 -> (가장 오래전 공격, i + j 작은, j 작은)
    max_value = 0
    mi, mj = -1, -1
    for i in range(N):
        for j in range(M):
            if matrix[i][j] == 0 or (i, j) == (si, sj):
                continue
            if max_value < matrix[i][j]:
                max_value = matrix[i][j]
                mi, mj = i, j
            elif max_value == matrix[i][j]:
                # 가장 오랜전에 공격(attack의 값이 작은)
                if attacked[mi][mj] > attacked[i][j]:
                    mi, mj = i, j
                elif attacked[mi][mj] == attacked[i][j]:
                    # 행 + 열의 합이 작은
                    if mi + mj > i + j:
                        mi, mj = i, j
                    elif mi + mj == i + j:
                        # 열의 값이 작은
                        if mj > j:
                            mi, mj = i, j
    return mi, mj


def find_path(si, sj, ei, ej):
    global matrix
    # (si, sj) -> (ei, ej)
    # 우, 하, 좌, 상 순 최단 거리 찾기 
    # 아래로 바로 가면 되는데 아닌데?

    q = deque([(si, sj)])
    # 이전에 온 위치를 기록한 visited
    visited = [[(-1, -1)] * M for _ in range(N)]
    visited[si][sj] = (0, 0)
    visited[si][sj] = (si, sj)

    path = []
    while q:
        ci, cj = q.popleft()

        # 도착
        if (ci, cj) == (ei, ej):
            path.append((ei, ej))
            ci, cj = ei, ej
            while True:
                if (ci, cj) == (si, sj):
                    return path

                ni, nj = visited[ci][cj]
                path.append((ni, nj))
                ci, cj = ni, nj

        # 우, 하, 좌, 상
        for di, dj in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
            ni, nj = (ci + di) % N, (cj + dj) % M
            # 미방문, 파괴된 포탑 x
            if matrix[ni][nj] > 0 and visited[ni][nj] == (-1, -1):
                q.append((ni, nj))
                # 자기의 이전 장소 기록
                # 이후에 갱신이 안됨(최소 거리)
                visited[ni][nj] = (ci, cj)
    # if문을 못만났으면 []
    return path


for turn in range(1, K + 1):
    # 공격에 참여했는지 안했는지 기록
    engaged = [[False] * M for _ in range(N)]

    # [1] 가장 약한 포탑 선정
    si, sj = find_attacker(matrix, attacked)

    matrix[si][sj] += (N + M)  # 공격력 증가
    attacked[si][sj] = turn  # 현재 공격 턴 기록
    engaged[si][sj] = True  # 공격 참여 기록
    attack_val = matrix[si][sj]  # 공격력

    # [2] 공격 대상 선정
    ei, ej = find_target(matrix, attacked, si, sj)

    # [3] 경로 찾기
    path = find_path(si, sj, ei, ej)

    if path != []:
        # [4] 레이저 공격
        # path에 (si, sj), (ei, ej)를 제거
        # 즉, 경로 내 포탑만 포함

        # 공격대상
        matrix[ei][ej] -= attack_val
        if matrix[ei][ej] <= 0:
            alive -= 1
        engaged[ei][ej] = True

        # 경로 내 포탑
        for ci, cj in path:
            if (ci, cj) == (si, sj) or (ci, cj) == (ei, ej):
                continue

            if matrix[ci][cj] > 0:
                matrix[ci][cj] -= attack_val // 2
                # 포탑 부서짐
                if matrix[ci][cj] <= 0:
                    alive -= 1
                engaged[ci][cj] = True
    else:
        # [5] 포탄 공격
        # 상, 우상, 우, 우하, 하, 좌하, 좌, 좌상
        # 공격 대상 공격
        matrix[ei][ej] -= attack_val
        if matrix[ei][ej] <= 0:
            alive -= 1
        engaged[ei][ej] = True

        # 주변 공격
        for di, dj in [(-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1)]:
            ni, nj = (ei + di) % N, (ej + dj) % M
            # 공격자 x, 주변 8개는 //2
            if (ni, nj) != (si, sj) and matrix[ni][nj] > 0:
                matrix[ni][nj] -= attack_val // 2
                # 포탑 부서짐
                if matrix[ni][nj] <= 0:
                    alive -= 1
                engaged[ni][nj] = True

    for i in range(N):
        for j in range(M):
            # [5] 포탑 부서짐
            if matrix[i][j] < 0:
                matrix[i][j] = 0
            # [6] 포탑 정비
            if matrix[i][j] > 0 and engaged[i][j] == False:
                matrix[i][j] += 1

    # 남은 포탑이 1개이면 종료
    if alive == 1:
        break

# 가장 강한 포탑의 공격력 출력
res = 0
for i in range(N):
    for j in range(M):
        if matrix[i][j] != 0:
            res = max(res, matrix[i][j])
print(res)

