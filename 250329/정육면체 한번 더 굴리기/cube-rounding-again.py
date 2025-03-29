# 정육면체 한번 더 굴리기
# 1이상 6이하 중 숫자가 그려진 NxN 격자판에 한 면이 1x1인 크기인 정육면체 존재
# 격자판에서 정육면체를 굴림

# 정육면체의 각 면에는 1 ~ 6 숫자가 쓰여져있고
# m번에 걸쳐 주사위를 계속 1칸씩 굴린다.
# 이때 마주보는 면에 적혀있는 숫자의 합은 정확히 7

# 항상 (0,0)에서 시작하고, 처음에는 항상 오른쪽으로 움직임

# 주사위를 움직일 때마다, 격자판 위 주사위가 놓여있는 칸에 적힌 숫자와
# 상하좌우로 인접하며, 같은 숫자가 적혀있는 모든 칸의 합만큼 점수를 얻는다
# (현재 칸에서 BFS로 같은 숫자일때만 이동?)
# 이게 맞는거같다

# 한 칸 이동 후,
# 주사위의 아랫면이 보드의 해당 칸에 있는 숫자보다 크면 현재 진행 방향에서 90도 시계방향 회전
# 아랫면이 칸의 숫자보다 작다면 현재 진행방향에서 90도 반시계방향 회전
# 같다면 현재 방향 유지

# 만약 진행 도중 격자판을 벗어나게 되면, 반사되어 이동 방향 반대로

# 이를 M번 반복
# M번 반복후 얻게되는 점수의 총합
from collections import deque

N, M = map(int, input().split())

board = [list(map(int, input().split())) for _ in range(N)]

dice = {"Up" : 1, "Down" : 6, "Right" : 3, "Left" : 4, "Front" : 2, "Back" : 5}
ci, cj = 0, 0
direction = "R"
d = {"R" : (0, 1), "L" : (0, -1), "U":(-1, 0), "D":(1, 0)}
score = 0
def move(dice, ci, cj, direction):
    
    # 현재 방향에서 한칸 이동 가능한지
    if direction == "R":
        direction = "L" if cj + 1 > N else "R"
    elif direction == "L":
        direction = "R" if cj - 1 < 0 else "L"
    elif direction == "U":
        direction = "D" if ci - 1 < 0 else "U"
    elif direction == "D":
        direction = "U" if ci + 1 > N else "D"
    di, dj = d[direction]
    ni, nj = ci + di, cj + dj

    # 회전
    if direction == "R":
        dice["Right"], dice["Left"], dice['Up'], dice['Down'], dice["Front"], dice["Back"] =\
        dice["Up"], dice["Down"], dice['Left'], dice['Right'], dice["Front"], dice["Back"] 
    elif direction == "L":
        dice["Left"], dice["Right"], dice['Down'], dice['Up'], dice["Front"], dice["Back"] =\
        dice["Up"], dice["Down"], dice['Left'], dice['Right'], dice["Front"], dice["Back"] 
    elif direction == "U":
        dice["Back"], dice["Front"], dice['Left'], dice['Right'], dice["Up"], dice["Down"] =\
        dice["Up"], dice["Down"], dice['Left'], dice['Right'], dice["Front"], dice["Back"] 
    elif direction == "D":
        dice["Front"], dice["Back"], dice['Left'], dice['Right'], dice["Down"], dice["Up"] =\
        dice["Up"], dice["Down"], dice['Left'], dice['Right'], dice["Front"], dice["Back"] 

    return dice, ni, nj, direction


def bfs(ci, cj):
    global score
    visited = [(ci, cj)]
    q = deque([(ci, cj)])
    curr_num = board[ci][cj]
    count = 1
    while q:
        ci, cj = q.popleft()
        for di, dj in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            ni, nj = ci + di, cj + dj
            if 0 <= ni < N and 0 <= nj < N and (ni, nj) not in visited and board[ni][nj] == curr_num:
                count += 1
                visited.append((ni, nj))
                q.append((ni, nj))
    score += curr_num * count


def find_direction(ci, cj, direction):
    # 아랫면 > 보드칸 : 90도 시계방향
    if dice["Down"] > board[ci][cj]:
        if direction == "R":
            direction = "D"
        elif direction == "L":
            direction = "U"
        elif direction == "U":
            direction = "R"
        elif direction == "D":
            direction = "L"
    # 아랫면 > 보드칸 : 90도 반시계방향  
    elif dice["Down"] < board[ci][cj]:
        if direction == "R":
            direction = "U"
        elif direction == "L":
            direction = "D"
        elif direction == "U":
            direction = "L"
        elif direction == "D":
            direction = "R"
    return direction


for _ in range(M):
    # 주사위가 현재 위치 ci, cj에서 direction 방향으로 이동
    dice, ci, cj, direction = move(dice, ci, cj, direction)
    # 현재 위치에서 같은 수를 가지는 칸 * 현재 칸 number 만큼 점수
    bfs(ci, cj)
    # 현재 칸을 기준으로 다음 방향 결정
    direction = find_direction(ci, cj, direction)
print(score)




