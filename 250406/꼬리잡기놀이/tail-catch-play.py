# 꼬리잡기 놀이

from collections import deque

# 격자 크기, 팀의 개수, 라운드 수
# N <= 20, M <= 5, # K <= 1000
N, M, K = map(int, input().split())

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


def dfs(ci, cj, visited, count):

    for di, dj in [(-1, 0), (1, 0), (0, 1), (0, -1)]:
        ni, nj = ci + di, cj + dj
        if is_range(ni, nj) and (ni, nj) not in visited:
            if board[ni][nj] == 2:
                visited.append((ni, nj))
                visited = dfs(ni, nj, visited, count + 1)
            if board[ni][nj] == 3 and count >= 2:
                visited.append((ni, nj))

    return visited

def make_team():
    for i in range(N):
        for j in range(N):
            if board[i][j] == 1:
                same_team = dfs(i, j, deque([(i, j)]), 1)
                teams.append(same_team)
                
def move():
    global board, teams

    # 보드 초기화 (0, 4 유지)
    new_board = [[4 if board[i][j] == 4 else 0 for j in range(N)] for i in range(N)]

    # 각 팀별로 이동
    for team in teams:
        # 현재 머리 위치 기준으로 이동 방향 찾기
        hi, hj = team[0]

        # 머리 위치의 주변 중 '4'인 칸이 다음 이동지
        next_head = team[-1]
        for di, dj in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            ni, nj = hi + di, hj + dj
            if is_range(ni, nj) and board[ni][nj] == 4:
                next_head = (ni, nj)
                break

        # 팀 위치 회전
        team.appendleft(next_head)  # 머리 앞으로 새 위치 추가
        tail = team.pop()           # 꼬리 제거 (이동 완료)

        # 이동 후 꼬리였던 자리는 이동선으로 변경됨
        tail_x, tail_y = tail
        new_board[tail_x][tail_y] = 4

        # board에 반영
        for idx, (x, y) in enumerate(team):
            if idx == 0:
                new_board[x][y] = 1
            elif idx == len(team) - 1:
                new_board[x][y] = 3
            else:
                new_board[x][y] = 2

    return new_board


# 라운드 별 공 던질 위치 확인
def find_pos(turn):
    mod_k = turn % (4 * N)

    bi, bj, d = -1, -1, -1

    # 상 0, 하 1, 좌 2, 우 3
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

def reverse_team(team):
    team.reverse()
    return team

def update_board(team):
    global board
    
    for i in range(len(team)):
        x, y = team[i]
        if i == 0:
            board[x][y] = 1
        elif i == len(team) - 1:
            board[x][y] = 3
        else:
            board[x][y] = 2

def get_score(bi, bj, d):
    global board
    
    di, dj = directions[d]

    while True:
        # 아무도 공을 받지 못함
        if not is_range(bi, bj):
            return 0
        
        if board[bi][bj] == 1 or board[bi][bj] == 2 or board[bi][bj] == 3:
            for i in range(len(teams)):
                if (bi, bj) in teams[i]:
                    ret = (teams[i].index((bi, bj)) + 1) ** 2
                    teams[i] = reverse_team(teams[i])
                    update_board(teams[i])
                    return ret
            
        bi += di
        bj += dj

res = 0

make_team()
for turn in range(K):
    # 각 팀 이동
    board = move()

    # # k 라운드 때 공 던지기
    bi, bj, d = find_pos(turn)
    
    res += get_score(bi, bj, d)
    

print(res)