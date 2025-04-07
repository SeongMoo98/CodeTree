# https://www.youtube.com/watch?v=y1_lca5hJHY&list=WL&index=66
'''
내 풀이)
같은 Team에 속한 것을 구할때 BFS를 통해 탐색했다
하지만 132222 이렇게 팀이 구해졌다(12223 순)
==> 탐색을 할 때 BFS만 하는 것이 아니라 BFS, DFS, Exhaustive search도 생각해야한다
'''
from h5py.h5o import visit

'''
문제 조건)
1. 각 팀은 머리사람을 따라 한칸 이동
2. 라운드마다 공이 정해진 선을 따라 던져진다(4n번째 라운드를 넘어가는 경우에는 다시 1라운드의 방향으로
3. 최초 공 맞은 사람(점수 획득 : 머리사람 기준 k번째면 k 제곱), 공을 획득한 경우 방향 바뀜

3 <= N <= 20, 1 <= M <= 5, 1 <= K <= 1000
0: 빈칸, 1: 머리, 2: 나머지, 3: 꼬리, 4: 이동선
'''

'''
풀이 Idea)
1. N x N x 팀 수 M x 턴수 1000 = > 20 x 20 x 5 x 1000 -> 시간이 넉넉해보인다
2. 팀 구성 : 순회하다가 1을 만나면 팀 구성(BFS)
3. 이동 : 머리의 이동 : 인접 4방향 중 4인 값으로 이동, 꼬리의 이동 : 끝에서 pop(), 그 좌표를 4로 수정
    하지만 머리랑 꼬리가 이어져있는 경우 : 머리에서 이동할 수 없다
    ==> 꼬리를 먼저 이동시키고 그 자리를 4로 만든 후 이동
4. 팀 구성할 때 BFS로 탐색할 떄 : 4방향, 범위내, 미방문, 다음 좌표가 2 or 직전좌표가 머리가 아니고 3
5. 공던지기
'''

N, M, K = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]

# 이동선이 4이므로 5부터 팀번호를 부여
teams = dict()
team_num = 5

from collections import deque
def bfs(si, sj, team_num):
    q = deque()
    q.append((si, sj))
    v[si][sj] = 1

    team = [(si, sj)]
    arr[si][sj] = team_num
    while q:
        ci, cj = q.popleft()

        # 네방향, 범위내, 미방문, 2 또는 출발지아닌 곳에서 오는 3
        for di, dj in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            ni, nj = ci + di, cj + dj
            if 0 <= ni < N and 0 <= nj < N and v[ni][nj]==0:
                if arr[ni][nj] == 2 or ((ci, cj) != (si, sj) and arr[ni][nj] == 3):
                    q.append((ni, nj))
                    v[ni][nj] = 1
                    arr[ni][nj] = team_num

    teams[team_num] = team

# [1] 팀 구성하기
v = [[0] * N for _ in range(N)]
for i in range(N):
    for j in range(N):
        # 머리 위치
        if v[i][j] == 0 and arr[i][j] == 1:
            bfs(i, j, team_num)
            team_num += 1

# 우, 상, 좌, 하
d = [(0, 1), (-1, 0), (0, -1), (1, 0)]
ans = 0
for k in range(K):
    # [1] 팀별 머리방향으로 한칸 이동
    for team in teams.values():
        ei, ej = team.pop() # 꼬리좌표 삭제
        arr[ei][ej] = 4     # 이동선으로 복원

        si, sj = team[0]
        for di, dj in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            ni, nj = si + di, sj + dj
            if 0 <= ni < N and 0 <= nj < N and arr[ni][nj] == 4:
                # 새 머리좌표, 맨 앞에 추가
                team.insert(0, (ni, nj))
                # 새 머리좌표에 팀 번호 적기
                arr[ni][nj] = arr[si][sj]
                break
    # [2] 라운드 번호에 맞게 시작위치 설정
    dr = (k // N)%4
    offset = k % N
    if dr == 0: # 우
        ci, cj = offset, 0
    elif dr == 1: # 상
        ci, cj = N-1, offset
    elif dr == 2: # 좌
        ci, cj = N-1-offset, N-1
    elif dr == 3: # 하
        ci, cj = 0, N-1-offset



    # [3] 공을 받은 사람 점수 추가 및 방향 바꾸기
    for i in range(N):
        # 최대 N번까지 탐색
        if 0 <= ci < N and 0 <= cj < N and arr[ci][cj] > 4:
            # 특정 팀 찾음
            team_n = arr[ci][cj]
            # 머리에서부터 (ci, cj)의 index + 1번째를 찾음
            ans += (teams[team_n].index(ci, cj)+1) ** 2
            teams[team_n] = teams[team_n][::-1]
            break
        ci, cj = ci + d[dr][0],cj +d[dr][1]
print(ans)