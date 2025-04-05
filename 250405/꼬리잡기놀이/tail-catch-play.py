# 꼬리잡기 놀이

# 3명 이상이 한팀
# 모든 사람들은 자신의 앞 사람의 허리를 잡고 움직인다(맨 앞에 있는 사람은 머리사람, 맨 뒤에 있는 사람은 꼬리 사람)
# 각 팀은 게임에서 주어진 이동 선을 따라서만 이동
# 각 팀의 이동선은 끝이 이어져있고, 각 팀의 이동선은 겹치지 않는다

# 한 라운드
# 1. 각 팀의 머리사람을 따라 한 칸 이동
# 2. 각 라운드마다 공이 정해진 선을 따라 던져짐
#    4n번째 라운드를 넘어가는 경우 다시 1라운드의 방향으로 돌아감


# 각 팀이 획득한 점수의 총합을 구하여라

from collections import deque

# 격자 크기, 팀의 개수, 라운드 수
# N <= 20
# M <= 5
# K <= 1000
N, M, K = map(int, input().split())

# 각 행에 해당하는 초기 상태
# 0 : 빈칸, 1 : 머리사람, 2: 꼬리사람이 아닌 나머지, 3: 꼬리사람, 4: 이동선

# 이동 선의 각 칸은 반드시 2개의 인접한 칸만이 존재(즉, 3방향으로 이동 x)
# ***** 각 칸은 2개의 인접한 칸만 존재하므로 각 팀의 이동선은 인접하지 않다 ***** # 
# 하나의 이동선에는 하나의 팀만이 존재

board = [list(map(int, input().split())) for _ in range(N)]
# teams의 내부 원소는 team(:deque)
# team[0] : 머리 사람

teams = []

# 상, 하, 좌 우
directions = {
    0: (-1, 0),
    1: (1, 0),
    2: (0, -1),
    3: (0, 1)
}

def is_range(i, j):
    return 0 <= i < N and 0 <= j <N


def make_team():
    global teams
    def bfs(si, sj):

        # (si, sj)는 머리사람
        q = deque([(si, sj)])
        visited = [(si, sj)]
        count = 1
        team = deque([(si, sj)])
        while q:
            ci, cj = q.popleft()

            if board[ci][cj] == 3:
                return team

            for di, dj in [(-1, 0), (0, 1), (1, 0), (0, -1)]:
                ni, nj = ci + di, cj + dj
                # 격자 안, 미방문, 중간사람, 꼬리사람
                if is_range(ni, nj) and (ni, nj) not in visited and (board[ni][nj] == 2 or board[ni][nj] == 3):
                    q.append((ni, nj))
                    visited.append((ni, nj))
                    team.append((ni, nj))


    for i in range(N):
        for j in range(N):
            # 머리 사람이라면 거기서 DFS 또는 BFS를 통해 team에 추가
            if board[i][j] == 1:
                same_team = bfs(i, j)
                teams.append(same_team)
                

def move():
    # 모든 사람들은 자신의 앞 사람의 허리를 잡고 움직인다(맨 앞에 있는 사람은 머리사람, 맨 뒤에 있는 사람은 꼬리 사람)
    # 각 팀은 게임에서 주어진 이동 선을 따라서만 이동
    global board, teams
    new_board = [[0] * N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            new_board[i][j] = board[i][j]

    for i in range(N):
        for j in range(N):
            # 머리 사람 이동
            if board[i][j] == 1:
                for team in teams:
                    if (i, j) in team:
                        for di, dj in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                            ni, nj = i + di, j + dj
                            if is_range(ni, nj) and board[ni][nj] == 4:
                                # board와 team 모두 이동
                                # 나머지 사람들은 앞사람의 좌표따라 이동
                                # 머리사람 이동
                                team.appendleft((ni,nj))
                                ei, ej = team.pop()
                                new_board[ei][ej] = 4
                                for k in range(len(team)):
                                    x, y = team[k]
                                    if k == 0:
                                        new_board[x][y] = 1
                                    elif k == len(team) - 1:
                                        new_board[x][y] = 3
                                    else:
                                        new_board[x][y] = 2
                                break
                                # 왜냐하면 나머지 사람들은 앞 사람 좌표 그대로 이용
    return new_board

# 라운드 별 공 던질 위치 확인
def find_pos(k):
    mod_k = k % (4 * N)
    bi, bj, d = -1, -1, -1
    if 0 <= mod_k < N:          # 우
        bi, bj, d = mod_k, 0, 3
    elif N <= mod_k < 2*N:      # 상
        mod_k -= N
        bi, bj, d = N-1, mod_k, 0
    elif 2*N <= mod_k < 3*N:    # 좌   
        mod_k -= 2 * N
        bi, bj, d = N-1 - mod_k, N-1, 2
    elif 3*N <= mod_k < 4*N:    # 하
        mod_k -= 3 * N
        bi, bj, d = 0, N-1 - mod_k, 1

    return bi, bj, d


def change(team):
    global board

    team.reverse()

    for i in range(len(team)):
        ci, cj = team[i]
        if i == 0:
            board[ci][cj] = 1
        elif i == len(team)-1:
            board[ci][cj] = 3
        else:
            board[ci][cj] = 2
    return team
def get_score(bi, bj, d):
    # 3. 공이 던져지는 경우 해당 선에 사람이 있으면 최초에 만나게 되는 사람만이 공을 얻어 점수를 얻음
    #    점수 : 해당 사람이 머리사람을 시작으로 팀 내에서 k번째 사람이라면 k^2만큼 점수
    #    아무도 공을 받지 못하면 점수 x

    # 공을 획득한 팀의 경우 머리사람과 꼬리 사람이 바뀜
    di, dj = directions[d]

    while True:
        # 아무도 공을 받지 못함
        if not is_range(bi, bj):
            return 0
        
        if board[bi][bj] == 1 or board[bi][bj] == 2 or board[bi][bj] == 3:
            for team in teams:
                for i in range(len(team)):
                    if (bi, bj) == team[i]:
                        team = change(team)
                        return i + 1
        bi += di
        bj += dj

res = 0

make_team()
for k in range(K):
    # 각 팀 이동
    board = move()

    # # k 라운드 때 공 던지기
    bi, bj, d = find_pos(k)
    
    res += get_score(bi, bj, d) ** 2

print(res)