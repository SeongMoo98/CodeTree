# N x N 격자, 승자 독식 모노폴리
# m개의 플레이어

# 1. 턴이 한번 진행될 때 각 플레이어는 한칸 이동
#    해당 칸에 이동했을 때 플레이어는 해당 칸을 독점 계약
#    초기 상태에 위치한 땅 역시 해당 플레이어의 독점 계약한 땅

# 2. 독점 계약은 K만큼의 턴 동안만 유효
#    K 턴이 지나게 되면 해당 칸은 다시 주인이 없는 칸

# 3. 각 플레이어는 각 방향별 이동 우선순위를 가진다.
#    우선 플레이어는 인접한 4방향 칸 중 아무도 독점계약을 하지 않은 칸으로 이동
#    그러한 칸이 없을 경우, 인접한 4방향 중 본인이 독점게약한 땅으로 이동
#    이동 가능한 칸이 여러개일 경우 이동 우선순위에 따라 움직일 칸을 결정
#    플레이어가 보고 있는 방향은 그 직전에 이동한 방향

# 4. 모든 플레이어가 이동한 후 한 칸에 여러 플레이어가 있을 경우 가장 작은 번호를 가진 플레이어만 살아남고
#    나머지 플레이어는 게임에서 사라짐



# 1번 플레이어만 남게되기까지의 걸린 턴의 수 출력(답이 1000 이상이거나, 불가능할 경우 -1 출력)

# 격자 크기 N, 플레이어 수 M, 턴 수 K
N, M, K = map(int, input().split())

# 격자 정보(0 : 빈칸, p : p번 플레이어 위치) + 턴 저장
grid = []
players = {}
alive = [-1] + [True] * M

for i in range(N):
    row = list(map(int, input().split()))
    for j in range(N):
        if row[j] == 0:
            row[j] = [0, 0]
        else:
            players[row[j]] = [i, j]
            row[j] = [row[j], K]
        
    grid.append(row)

# 각 플레이어의 초기 방향
# 상 : 1, 하 : 2, 좌 : 3, 우 : 4
init_dir = [-1] + list(map(int, input().split()))
for i in range(1,M+1):
    players[i].append(init_dir[i])

# 각 플레이어의 이동우선 순위
from collections import defaultdict
prior_dir = defaultdict(dict)

for i in range(1, M+1):
    for dir in range(1, 5):
        # i player의 dir 별 우선순위
        prior_dir[i][dir] = list(map(int,(input().split())))


turn = 0
# 상, 하, 좌, 우
d = {1: (-1, 0), 2: (1, 0), 3: (0, -1), 4: (0, 1)}

# turn이 1000번 미만이거나, 1번외 1명의 player가 더 살아있으면 계속 진행
while turn < 1000 and (alive[1] == True and alive.count(True) >= 2):
    # 각 플레이어 이동(우선순위 확인)
    # 플레이어는 인접한 4방향 칸 중 아무도 독점계약을 하지 않은 칸으로 이동
    # 그러한 칸이 없을 경우, 인접한 4방향 중 본인이 독점게약한 땅으로 이동
    # 이동 가능한 칸이 여러개일 경우 이동 우선순위에 따라 움직일 칸을 결정
    # 플레이어가 보고 있는 방향은 그 직전에 이동한 방향

    for p in range(1, M+1):
        if alive[p]:
            ci, cj, curr_dir = players[p][0], players[p][1], players[p][2]

            for next_dir in prior_dir[p][curr_dir]:
                ni, nj = ci + d[next_dir][0], cj + d[next_dir][1]
                # 범위 내, 독점 계약 x
                if 0 <= ni < N and 0 <= nj < N and grid[ni][nj][0] == 0:
                    # Player 이동
                    players[p] = [ni, nj, next_dir]
                    break

                    # 이 때 grid를 수정해서 다음 Player가 못 들어오게 하는게 아니라
                    # 모두 다 움직이고 난 다음에 겹치는 게 있다면 작은 Player가 살아남음
                    # grid[ni][nj] =     
            # 4 방향 모두 독점계약 되어있다.
            else:
                for next_dir in prior_dir[p][curr_dir]:
                    ni, nj = ci + d[next_dir][0], cj + d[next_dir][1]
                    # 범위 내, 독점 계약 x
                    if 0 <= ni < N and 0 <= nj < N and grid[ni][nj][0] == p:
                        # Player 이동
                        players[p] = [ni, nj, next_dir]
                        break

    # grid 반영하기(같은 칸에 있을 수 있다)
    for p in range(1, M+1):
        if alive[p] == 0:
            continue
        i, j = players[p][0], players[p][1]
        for fight_p in range(p+1, M+1):
            if alive[fight_p] == 0:
                continue
            if (i, j) == (players[fight_p][0], players[fight_p][1]):
                alive[fight_p] = False       
        grid[i][j][0], grid[i][j][1] = p, K


    # 독점 계약 갱신
    for i in range(N):
        for j in range(N):
            # 독점계약이 되어있고, 그 Player의 현재 위치가 거기가 아니면 -1
            p = grid[i][j][0]
            if grid[i][j][0] != 0 and (players[p][0], players[p][1]) != (i, j) :
                grid[i][j][1] -= 1
                # 계약 종료
                if grid[i][j][1] == 0:
                    grid[i][j] = [0, 0]   

    turn += 1

if turn >= 1000:
    print(-1)
else:
    print(turn)
