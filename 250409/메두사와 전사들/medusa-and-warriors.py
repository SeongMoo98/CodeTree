'''
메두사와 전사들

N x N 격자 (도로 0, 비도로 1)

메두사 : 집(S_r, S-c) -> 공원(E_r, E-c) 최단 경로, 항상 도로 위, 둘 좌표는 다름
M명의 전사 : 초기 (r_i, c_i) -> 메두사 최단경로, 도로, 비도로 가리지 않음, 초기 전사들의 위치는 메두사의 집 x
최단거리 : 맨해튼 거리
메두사는 전사들이 "움직이기 전"에 돌로 만듬


[1] 메두사의 이동
    공원까지 도로를 따라 최단거리(전사가 있을 경우 전사 사라짐)
    상, 하, 좌, 우 우선순위
    집 -> 공원 경로 "없을 수도 있다"

[2] 메두사의 시선
    상, 하, 좌, 우 중 한 곳 바라봄
    90도의 시야각, 전사를 바라봄
    시야각에 들어왔지만 다른 전사에 가려진 경우 보이지 않는다
    메두사에게 가려지는 범위
        메두사로부터 8방향중 한 방향에 전사가 위치해 있다면, 그 전사가 동일한 방향으로 바라본 범위에
        포함된 모든 칸에는 메두사가 보이지 않는다
    메두사가 본 전사들은 해당 턴에 움직일 수 없고, 이번 턴이 종료되면 해제(둘 이상 있으면 둘다)

    메두사의 시선 방향
        (1) 전사를 가장 많이 볼 수 있는 (2) 상, 하, 좌, 우 우선순위

[3] 전사들의 이동
    돌로 변하지 않은 전사들은 메두사를 향해 최대 2칸 이동(같은 칸에 2명 이상 가능)
    (1) 첫번째 이동
        메두사와 거리를 줄일 수 있는 방향(상, 하, 좌, 우 우선)
        격자 밖 x, 메두사의 시야에는 안됨

    (2) 두번째 이동
        메두사와 거리를 줄일 수 있는 방향(좌, 우, 하, 상 우선)
        격자 밖 x, 메두사의 시야는 안됨

[4] 전사의 공격
    메두사와 같은 칸이면 메두사를 공격하지만 이기지 못하고 "사라짐"

위의 4단계를 반복하여 메두사가 공원에 도달할 때까지
매 턴마다 해당 턴에서 모든 전사가 이동한 거리의 합, 돌로 변한 전사의 수, 메두사를 공격한 전사의 수를 출력
메두사가 공원에 도착하는 턴에는 0을 출력하고 종료
만약 메두사 -> 공원 경로가 없다면 -1 출력(처음)

마을의 크기 N, 전사의 수 M
0 <= N <= 50, 0 <= M <= 300
'''
from collections import deque


N, M = map(int, input().split())
# 메두사의 집, 공원
si, sj, ei, ej = map(int, input().split())

# (i, j)에 있는 전사의 수
warriors = [[0] * N for _ in range(N)]
# 해당 턴에 돌인지
stone = [[False] * N for _ in range(N)]


temp = list(map(int ,input().split()))
for i in range(0, len(temp), 2):
    x, y = temp[i], temp[i+1]
    warriors[x][y] += 1

arr = [list(map(int, input().split())) for _ in range(N)]

def is_range(x, y):
    return 0 <= x < N and 0 <= y < N

def find_block_direction(si, sj, wi, wj, curr_d):
    if curr_d == 0:     # 상
        if cj > wj: wd = [(-1, -1), (-1, 0)]  # 좌상, 상
        elif cj == wj: wd = [(-1, 0)]          # 상
        elif cj < wj: wd = [(-1, 0), (-1, 1)] # 상, 우상
    elif curr_d == 1:   # 하
        if cj > wj: wd = [(1, -1), (1, 0)]    # 좌하 ,하
        elif cj == wj: wd = [(1, 0)]          # 하
        elif cj < wj: wd = [(1, 0), (1, 1)]   # 하, 우하

    elif curr_d == 2:   # 좌
        if ci > wi: wd = [(-1, -1), (0, -1)]  # 좌상, 좌
        elif ci == wi: wd = [(0, -1)]         # 좌
        elif ci < wi: wd = [(0, -1), (1, -1)] # 좌, 좌하

    elif curr_d == 3:    # 우
        if ci > wi: wd = [(-1, 1), (0, 1)]    # 우상, 우
        elif ci == wi: wd = [(0, 1)]          # 우
        elif ci < wi: wd = [(0, 1), (1, 1)]   # 우하, 우
    return wd


def look(si, sj):
    # 메두사의 현재 위치를 시작으로 blocked를 처리

    # 상, 하, 좌, 우 4번 돌고 (count, dir) 정렬
    # 그떄의 blocked return

    # 상(0): 좌상, 상, 우상
    # 하(1): 좌하, 하, 우하
    # 좌(2): 좌상, 좌, 좌하
    # 우(3): 우상, 우, 우하
    directions = {
        0: [(-1, -1), (-1, 0), (-1, 1)],
        1: [(1, -1), (1, 0), (1, 1)],
        2: [(-1, -1), (0, -1), (1, -1)],
        3: [(-1, 1), (0, 1), (1, 1)]
    }
    # 4방향에 대하 메두사의 시선
    temp_lst = []
    for curr_d in range(4):
        q = deque()
        visited = [[False] * N for _ in range(N)]

        # 메두사 시야 밖 처리도 해야함 !
        # 애초에 시야 밖에 있는 좌표
        blocked = [[True] * N for _ in range(N)]

        q.append((si, sj))
        visited[si][sj] = True

        while q:
            ci, cj = q.popleft()

            # 현재 기준 3방향 이동
            for di, dj in directions[curr_d]:
                ni, nj = ci + di, cj + dj
                # 세방향, 미방문, 가려지지 않은 곳
                if is_range(ni, nj) and visited[ni][nj] == False:
                    q.append((ni, nj))
                    visited[ni][nj] = True
                    blocked[ni][nj] = False

        cnt = 0
        '''
        앞에 있는 게 먼저 되는게 아니라 뒤에 있는게 먼저 시작해버리네;;        
        '''
        for wsi in range(N):
            for wsj in range(N):
                if warriors[wsi][wsj] > 0 and blocked[wsi][wsj] == False:

                    nq = deque()
                    n_visited = [[False] * N for _ in range(N)]

                    nq.append((wsi, wsj))
                    n_visited[wsi][wsj] = True
                    while nq:
                        wci, wcj = nq.popleft()
                        # 현재 메두사의 위치, 현재 전사의 위치, 현재 메두사 시야 방향으로 방향 결정
                        wd = find_block_direction(si, sj, wsi, wsj, curr_d)

                        for wdi, wdj in wd:
                            wni, wnj = wci + wdi, wcj + wdj
                            # 범위내, 미방문 -> blocked 처리
                            if is_range(wni, wnj) and n_visited[wni][wnj] == False:
                                nq.append((wni, wnj))
                                n_visited[wni][wnj] = True
                                blocked[wni][wnj] = True

        for wi in range(N):
            for wj in range(N):
                # 전사 있고, block 되지 못한곳
                if warriors[wi][wj] > 0 and blocked[wi][wj] == False:
                    cnt += warriors[wi][wj]
        temp_lst.append((cnt, curr_d, blocked))
    # 돌로 만든 전사의 수 많은, 상 하 좌 우 순
    temp_lst.sort(key=lambda x: (-x[0], x[1]))

    ret_cnt, ret_dir, ret_blocked = temp_lst[0]

    return ret_cnt, ret_dir, ret_blocked



def find_path(si, sj, ei, ej):
    q = deque()
    visited = [[(-1, -1)] * N for _ in range(N)]

    q.append((si, sj))
    visited[si][sj] = (si, sj)

    while q:
        ci, cj = q.popleft()

        if (ci, cj) == (ei, ej):
            path = [(ci, cj)]
            while True:
                if (ci, cj) == (si, sj):
                    return path[::-1]
                ni, nj = visited[ci][cj]
                path.append((ni, nj))
                ci, cj = ni, nj
        # 상하좌우
        for di, dj in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            ni, nj = ci + di, cj + dj
            if is_range(ni, nj) and visited[ni][nj] == (-1, -1) and arr[ni][nj] == 0:
                q.append((ni, nj))
                visited[ni][nj] = (ci, cj)

    return -1

# [1] 메두사의 집 -> 공원 경로 찾기
path = find_path(si, sj, ei, ej)

if path != -1:
    # path[0]은 초기위치라 다음 칸부터 시작
    for i in range(1, len(path)):
        dist, stone_cnt, attack_cnt = 0, 0, 0
        ci, cj = path[i]

        # 메두사가 공원에 도착했으면 0 출력 후 종료
        if (ci, cj) == (ei, ej):
            print(0)
            break

        # 메두사가 이동해서 전사 사라짐
        for wi in range(N):
            for wj in range(N):
                if warriors[wi][wj] > 0 and (ci, cj) == (wi, wj):
                    warriors[wi][wj] = 0

        # [2] 메두사의 시선
        stone_cnt, curr_d, blocked = look(ci, cj)

        # 돌처리
        for wi in range(N):
            for wj in range(N):
                if warriors[wi][wj] > 0 and blocked[wi][wj] == False:
                    stone[wi][wj] = True



        # [3] 전사 이동 & 공격
        # 첫번째, 두번째 이동방향
        dirs = {
            1: [(-1, 0), (1, 0), (0, -1), (0, 1)], # 상하좌우
            2:  [(0, -1), (0, 1), (-1, 0), (1, 0)] # 좌우상하
        }
        '''
            for문을 사용할때는 항상 조심해라
        '''
        n_warriors = [x[:] for x in warriors]
        for step in range(1, 3):
            for wi in range(N):
                for wj in range(N):
                    # 전사 아니거나, 해당 턴에 돌이면 pass
                    if warriors[wi][wj] <= 0 or stone[wi][wj] == True:
                        continue
                    # 이동(최단거리, 상하좌우(1), 좌우하상(2))
                    # 어차피 모두 갈 수 있기 때문에 먼저 갈 수 있는 곳이 최단거리
                    for di, dj in dirs[step]:
                        ni, nj = wi + di, wj + dj

                        # 미방문, 거리 감소, 시야에 가린 or 시야 밖(즉, blocked 안된 곳)
                        if is_range(ni, nj) and abs(ci - ni) + abs(cj - nj) < abs (ci - wi) + abs(cj - wj) and blocked[ni][nj] == True:
                            n_warriors[ni][nj] += warriors[wi][wj]
                            dist += warriors[wi][wj]
                            # 이동한 곳이 메두사의 위치라면
                            if (ni, nj) == (ci, cj):
                                attack_cnt += warriors[wi][wj]
                                n_warriors[ni][nj] = 0
                            n_warriors[wi][wj] = 0
                            break

            warriors = [x[:] for x in n_warriors]


        # 돌로 변한 전사 되돌림
        for wi in range(N):
            for wj in range(N):
                if stone[wi][wj] == True:
                    stone[wi][wj] = False

        print(dist, stone_cnt, attack_cnt)

else:
    # path가 없다면 -1 출력
    print(path)





