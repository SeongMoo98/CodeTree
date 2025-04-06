# 싸움땅
# N x N 격자, 각 격자에는 무기들이 존재

# 초기에는 무기들이 없는 빈 격자에 플레이어들이 위치하며, 초기 능력치를 지닌다(초기 능력치는 모두 다름)

# 총 : 공격럭, 플레이어 : 능력치, 플레이어 번호



# 위 과정을 1 ~ N번 플레이어까지 순차적으로 진행하면 1라운드 끝
# K 라운드 동안 게임을 진행하면서 각 플레이어들이 획득한 포인트 출력

# 격자 크기, 플레이어 수, 라운드 수
# N <= 20, M <= 30, k <= 500
N, M, K = map(int, input().split())

matrix = [[] for _ in range(N)]
# (능력치, 가진 총, 방향)
players_info = [[0, 0, 0]] * M
# (i, j)
players_pos = [[0, 0]] * M 
scores = [0] * M

directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
for i in range(N):
    for j in range(N):
        matrix[i].append([])

# 총 정보
for i in range(N):
    guns = list(map(int, input().split()))
    for j in range(N):
        if guns[j] != 0:
            matrix[i][j].append(guns[j])

# 플레이어 정보
# 플레이어의 위치는 겹쳐서 주어지지 않고, 초기 위치에는 총이 주어지지 않는다.
for i in range(M):
    # d : 상(0), 우(1), 하(2), 좌(3)
    x, y, d, s = map(int, input().split())
    x, y = x-1, y-1
    players_info[i] = [s, 0, d]
    players_pos[i] = [x, y]

def is_range(i, j):
    return 0 <= i < N and 0 <= j < N

def get_gun(idx):
    # 해당 칸에 총이 있고 플레이어에게 총이 없다면, 해당 플레이어는 총 획득
    # 해당 칸에 총이 있고 플레이어에게 총이 있다면, 가지고 있는 총과 놓여있는 총들 중 공격력이 가장 큰 총 획득
    # 나머지 총들은 해당 격자에 둔다
    global matrix, players_info, players_pos
    x, y = players_pos[idx]
    if matrix[x][y] != []:
        max_gun = max(matrix[x][y])
        
        # 총을 집고 나머지는 내려놓음
        if max_gun > players_info[idx][1]:
            max_gun_idx = matrix[x][y].index(max_gun)
            # 총을 가지고 있을 때 내려놓음
            if players_info[idx][1] != 0:
                matrix[x][y].append(players_info[idx][1])
            matrix[x][y].pop(max_gun_idx)
            return max_gun
        else:
            # 원래 가지고 있던 총 유지
            return players_info[idx][1]
    else:
        # 원래 가지고 있던 총 유지
        return players_info[idx][1]

def figth(idx1, idx2):
    # idx1이 움직인 player, idx2가 원래 있던 player
    global players_info, players_pos, scores
    #    해당 플레이어의 초기 능력치 + 총의 공격력의 합을 비교하면 큰 사람이 이김
    #    만약 수치가 동일한 경우 초기 능력치가 높은 플레이어가 승리
    #    이긴 플레이어는 초기 능력치와 가지고 있는 총의 공격력 합의 차이만큼 포인트를 획득
    if players_info[idx1][0] + players_info[idx1][1] > players_info[idx2][0] + players_info[idx2][1]:
        win_idx, lose_idx = idx1, idx2
    elif players_info[idx1][0] + players_info[idx1][1] == players_info[idx2][0] + players_info[idx2][1]:
        if players_info[idx1][0] > players_info[idx2][0]:
            win_idx, lose_idx = idx1, idx2
        else:
            win_idx, lose_idx = idx2, idx1
    else:
        win_idx, lose_idx = idx2, idx1

    # 점수 획득
    scores[win_idx] += (players_info[win_idx][0] + players_info[win_idx][1]) - (players_info[lose_idx][0] + players_info[lose_idx][1])

    # 4. 진 플레이어는 본인이 가지고 있던 총을 해당 격자에 내려놓고, 가지고 있던 방향으로 한칸 이동
    #    이동하려는 칸에 플레이어가 있거나, 격자 범위 밖인 경우 오른쪽으로 90도 회전 -> 빈칸으로 이동
    #    이동하려는 칸에 총이 있다면, 가장 높은 공격력이 높은 총을 획득하고, 나머지 총들은 해당 격자에 내려놓음
    li, lj = players_pos[lose_idx]
    # 총 내려놓음(총이 있을 때)
    if players_info[lose_idx][1] != 0:
        matrix[li][lj].append(players_info[lose_idx][1])
        players_info[lose_idx][1] = 0

    while True:
        d = players_info[lose_idx][2]
        ni, nj = li + directions[d][0], lj + directions[d][1]
        # 격자 안이고 플레이어 없다면
        if is_range(ni, nj) and [ni, nj] not in players_pos:
            players_pos[lose_idx] = [ni, nj]
            players_info[lose_idx][1] = get_gun(lose_idx)
            break
        else:
            players_info[lose_idx][2] = (players_info[lose_idx][2] + 1) % 4
    
    # 5. 이긴 플레이어는 승리한 칸에 떨어져 있는 총들과 원래 들고있던 총 중 가장 높은 공격력이 높은 총을 획득하고
    #    나머지 총은 해당 격자에 내려놓음
    players_info[win_idx][1] = get_gun(win_idx)

    

def move_player(idx):
    global players_info, players_pos
    # 1. 플레이어는 본인이 향하고 있는 방향대로 한칸 이동(격자를 벗어나는 경우 정반대로 방향 바꿔서), 상하좌우
    # stat, gun, d = players_info
    d = players_info[idx][2]
    ni, nj = players_pos[idx][0] + directions[d][0], players_pos[idx][1] + directions[d][1]

    # 격자 밖이면 방향 바꿈
    if not is_range(ni, nj):
       players_info[idx][2] = (players_info[idx][2] + 2) % 4
       d = players_info[idx][2]
       ni, nj = players_pos[idx][0] + directions[d][0], players_pos[idx][1] + directions[d][1]
    
    # 2. 이동한 칸에 플레이어가 없다면 해당 칸에 총이 있는지 확인
    if [ni, nj] not in players_pos:
        players_pos[idx] = [ni, nj]
        if matrix[ni][nj] != []:
            players_info[idx][1] = get_gun(idx)
    else:
        # 3. 이동한 칸에 플레이어가 있다면 두 플레이어는 싸운다
        player2_idx = players_pos.index([ni, nj])
        players_pos[idx] = [ni, nj]
        figth(idx, player2_idx)
        
for turn in range(K):
    for i in range(M):
        move_player(i)

for i in range(M):
    print(scores[i], end=' ')


