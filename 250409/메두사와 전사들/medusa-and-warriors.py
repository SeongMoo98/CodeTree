'''
"또한, Matrix 한 칸에 여러명이 존재할 수 있다" : Matrix 안에 List 또는 숫자로 표시하는 걸 생각해라
    dict로 풀다가 애매해졌네
전사 이동에서 Matrix에 적용이 제대로 되지 못했다
'''

'''
문제 조건)
1. 메두사의 이동
    도로를 따라 최단거리(상하좌우)
    인접한 칸에 전사 있으면, 전사 사라짐
2. 메두사의 시선
    가장 많이 돌로 만드는 방향(상하좌우)
    8방향 중 한 방향에 전사가 위치하면, 그 전사가 동일한 방향으로 바라본 범위의 칸은 안보임
3. 전사들의 이동
    메두사 쪽으로 최단거리 이동
    첫번째 이동 : 상하좌우
    두번째 이동 : 좌우상하
4. 전사의 공격   
    공격 후 사라짐

입력
4 <= N <= 50 , 0 <= M <= 300

출력
이동 합, 돌이됭 수, 공격 수
'''

'''
풀이 Idea)
[1] 메두사의 이동
    한번만 BFS 처리 -> 경로 없으면 -1
    BFS 이동 경로 처리(상하좌우)
[2] 메두사의 시선
'''

from collections import deque
def find_route(si, sj, ei, ej):
    q = deque()
    visited =[[0] * N for _ in range(N)]

    q.append((si, sj))
    visited[si][sj] = ((si, sj))

    while q:
        ci, cj = q.popleft()
        if (ci, cj) == (ei, ej):
            '''
                내가 짠 코드는 시작위치를 포함한 route 였는데
                이렇게 짜면 시작점 바로 다음 좌표의 경로이다
            '''
            route = []
            ci, cj = visited[ci][cj]
            while (ci, cj) != (si, sj):
                route.append((ci, cj))
                ci, cj = visited[ci][cj]
            return route[::-1]

        # 상하좌우 순
        for di, dj in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            ni, nj = ci + di, cj + dj
            if 0 <= ni < N and 0 <= nj < N and visited[ni][nj] == 0 and arr[ni][nj] == 0:
                q.append((ni, nj))
                visited[ni][nj] = (ci, cj)

    return -1

def mark_line(v, ci, cj, dr):
    while 0 <= ci < N and 0 <= cj < N:
        v[ci][cj] = 2                       # 시각적 구분 위해 2로 표시
        ci, cj = ci + di[dr], cj + dj[dr]   # 해당 방향으로 한 칸 이동

def mark_safe(v, si, sj, dr, org_dr):
    # [1] 직선방향 표시
    ci,cj = si+di[dr], sj+dj[dr]
    # v에 dr방향으로 이동가능지역 표시
    mark_line(v, ci, cj, dr)

    # [2] 바라보는 방향으로 한줄씩 표시
    ci,cj = si+di[org_dr],sj+dj[org_dr]
    # 범위 내리면서 계속 진행
    while 0<=ci<N and 0<=cj<N:
        # v에 dr방향으로 이동가능지역 표시
        mark_line(v, ci, cj, dr)
        ci,cj = ci+di[org_dr],cj+dj[org_dr]

def make_stone(marr, mi, mj, dr):
    # 현재 칸에서 dr방향으로 쭉 이동하고
    # 대각 방향으로 한칸 옮겨서 다시 dr방향으로 쭉 이동

    v = [[0]*N for _ in range(N)]
    cnt = 0
    # [1] dr 방향으로 전사 만날때 까지 1 표시(메두사의 시야), 그 후 2 표시(가려짐)
    ni, nj = mi + di[dr], mj + dj[dr]
    while 0 <= ni < N and 0 <= nj < N:
        v[ni][nj] = 1
        if marr[ni][nj] > 0:
            # 돌로 변한 기사의 수
            cnt += marr[ni][nj]
            # 동일 방향으로 이동
            ni, nj = ni + di[dr], nj + di[dr]
            # v에 dr방향으로 이동처리
            mark_line(v, ni, nj, dr)
            break
        ni, nj = ni + di[dr], nj + dj[dr]

    # [2] dr-1, dr+1 방향으로 동일 처리, 대각선 원점 잡고 dr방향으로 이동
    for org_dr in ((dr - 1) * 8, (dr + 1) % 8):
        # 첫 대각선 위치부터 체크
        si, sj = mi + di[org_dr], mj + dj[org_dr]
        # 대각선 방향으로 초기 위치 탐색후 직선 단위 처리
        while 0 <= si < N and 0 <= sj < N:
            # 전사 만나면 전사가 바라보는 방향 처리
            if v[si][sj] == 0 and marr[si][sj] > 0:
                v[si][sj] = 1
                cnt += marr[si][sj]  # 돌로만든 전사수 누적
                # v에 dr방향으로 이동가능지역 표시
                # 직선으로 이동하는 방향, 대각 방향으로 둘다 표시
                mark_safe(v, si, sj, dr, org_dr)
                break

            # 첫 위치가 전사가 아닌 경우는 직선으로 내려오며 탐색
            ci, cj = si, sj
            while 0 <= ci < N and 0 <= cj < N:  # 범위내라면 계속 진행
                # 처음 방문
                if v[ci][cj] == 0:
                    v[ci][cj] = 1
                    # 전사로 막혔으면
                    if marr[ci][cj] > 0:
                        cnt += marr[ci][cj]
                        # v에 dr방향으로 이동가능지역 표시
                        mark_safe(v, ci, cj, dr, org_dr)
                        break
                else:
                    break
                ci, cj = ci + di[dr], cj + dj[dr]

            # 기준점 변경
            si, sj = si + di[org_dr], sj + dj[org_dr]

    return v, cnt


def move_men(v, mi, mj):

    # (1) 상하좌우, (2) 좌우상하
    move, attack = 0, 0

    for dirs in (((-1,0),(1,0),(0,-1),(0,1)), ((0,-1),(0,1),(-1,0),(1,0))):
        for idx in range(len(men)-1, -1, -1):
            ci, cj = men[idx]
            if v[ci][cj] == 1:
                continue

            dist = abs(mi - ci) + abs(mj - cj)
            for di, dj in dirs:
                ni, nj = ci + di, cj + dj
                # 범위내, 메두사 아니고, 현재보다 줄어드는 방향
                if 0 <= ni < N and 0 <= nj < N and v[ni][nj] != 1 and dist > abs(mi-ni) + abs(mi-nj):
                    if (ni, nj) == (mi, mj):
                        attack += 1
                        men.pop(idx)
                    else:
                        men[idx] = [ni, nj]
                    move += 1
                    break

    return move, attack

###################################################
###################################################

N, M = map(int, input().split())
si, sj, ei, ej = map(int, input().split())
t_lst = list(map(int, input().split()))

men = []
for i in range(0, 2*M, 2):
    men.append([t_lst[i], t_lst[i+1]])
arr = [list(map(int, input().split())) for _ in range(N)]


route = find_route(si, sj, ei, ej)

if route == -1:
    print(-1)
else:
    for mi, mj in route:
        move_cnt, attack_cnt = 0, 0
        # [1] 메두사 이동 : 지정된 최단 거리로 한칸 이동, 전사 사라짐 처리
        ''' 
            삭제시는 역순으로 제거하는게 편하다
            왜냐하면 위에서부터 삭제하면 아래의 Element가 위로 올라와서 다음 순회할 Element의 index가 바뀌게 된다 
        '''
        # 메두사가 이동했을 때 삭제 처리
        for i in range(len(men)-1, -1, -1):
            if men[i] == [mi, mj]:
                men.pop(i)


        # [2] 메두사의 시선 : 상하좌우 네 방향 중 가장 많이 돌로 만들 수 있는 방향 찾기
        # ==> v[]에 표시에서 이동시 참조(메두사의 시선 == 1, 전사에 가려진 곳 == 2, 빈땅 == 0)

        # 상,우상, 우,우하, 하,좌하, 좌,좌상
        # 0,  1,  2,  3,  4,  5,  6,  7
        di = [-1, -1, 0, 1, 1, 1, 0, -1]
        dj = [0, 1, 1, 1, 0, -1, -1, -1]

        # marr[][] : 지도에 있는 전사 수
        marr = [[0] * N for _ in range(N)]
        for ti, tj in men:
            marr[ti][tj] += 1

        max_stone = -1
        v = []
        # 상하좌우
        for dr in [0, 4, 6, 2]:
            tv, tstone = make_stone(marr, mi, mj, dr)
            if max_stone < tstone:
                max_stone = tstone
                v = tv

        # [3] 전사들의 이동(한칸 씩 두번) : 메두사가 있는 경우 공격 후 사라짐
        move_cnt, attack_cnt = move_men(v, mi, mj)


        print(move_cnt, max_stone, attack_cnt)
    print(0)