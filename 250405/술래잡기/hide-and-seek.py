# N x N 격자에서 진행되는 술래잡기 게임
# 처음엔 정중앙에서 시작

# m명의 도망자
# 도망자의 종류는 좌우로만 움직이는 유형, 상하로만 움직이는 유형 2가지
# 좌우로 움직이는 사람 : 항상 오른쪽을 보고 시작
# 상하로 움직이는 사람 : 항상 아래쪽을 보고 시작

# h개의 나무
# 나무와 도망자가 초기에 겹쳐져 주어지는 것 역시 가능

# m명의 도망자가 먼저 동시에 움직이고, 술래가 움직임
# 이렇게 도망자 1턴, 술래가 1턴 진행하는 것을 k번 반복


# 이를 k번에 걸쳐 술래잡기를 진행하는 동아 술래가 총 얻게된 점수 출력

# 격자 크기(홀수), 도망자 수, 나무 수, 턴 수
# n <= 99
# m, h <= n ^ 2 ==> 10^5
# k <= 100
N, M, H, K = map(int, input().split())

# (이동 방향, 보는 방향) => 결국 같다 
# ==> 이동 방향만 저장
run = [[] for _ in range(N)]
for i in range(N):
    for j in range(N):
        run[i].append([])
    
    
tree = [[False] * N for _ in range(N)]
# 도망자의 위치(겹칠 수 있음)
# list를 원소로하는 2차원 array
# (x, y)에서 d
# d=1 : 좌우(오른쪽 보고 시작), d=2 : 상하(아래보고 시작)

# 상 : 0, 우 : 1, 하 : 2, 좌 : 3
directions = {
    0: (-1, 0),
    1: (0, 1),
    2: (1, 0),
    3: (0, -1)
}

for _ in range(M):
    ri, rj, d = map(int, input().split())
    ri, rj = ri-1, rj-1
    # d=1 : 좌우 이동(우 로 시작)
    # d=2 : 상하 이동(하 로 시작)
    run[ri][rj].append(d)

# 나무 위치(겹칠 수 없음)
# ==> 2차원 Array
for _ in range(H):
    ti, tj = map(lambda x:int(x)-1, input().split())
    tree[ti][tj] = True


# 술래 초기 위치(격자 중앙)
si, sj = N//2, N//2
# 술래 초기 방향 : 상
s_dir = 0

# -----------------------------------------------------------# 
# 술래 움직임
# 처음 위 방향으로 시작해서 달팽이 모양으로 움직임
# 상(0) 1 -> 우(1) 1 -> 하(2) 2 -> 좌(3) 2 -> 상(0) 3 -> 우(1) 3 -> 하(2) 4 -> 좌(3) 4 -> 상(0) 4
# ==> s_dir 이 홀수이면 이동 칸 수 + 1(마지막 제외)

# 만약 끝 (0, 0)에 도달하게 되면 다시 거꾸로 중심으로 이동하고, 다시 중심으로 오게 되면 처음처러 달팽이 방향으로 돈다
# 하(2) 4 -> 우(1) 4 -> 상(0) 4 -> 좌(3) 3 -> 하(2) 3 -> 우(1) 2 -> 상(0) 2 -> 좌(3) 1 -> 하(0) 1
# ==> s_di이 짝수이면 이동 칸 수 - 1(처음 제외)
# (중앙에서 시작하는 것과 반대 방향이지만 이동 칸 수는 똑같이)
# -----------------------------------------------------------# 
def make_mode():
    mode = {
        "center_start" :[],
        "zero_start":[]
    }
    # center에서 시작
    cx, cy = N//2, N//2
    c_dir = 0
    move_num = 1
    while (cx, cy) != (N-1, 0):
        for _ in range(move_num):
            dx, dy = directions[c_dir]
            nx, ny = cx + dx, cy + dy
            
            mode["center_start"].append(c_dir)
            cx, cy = nx, ny

        if c_dir % 2 == 1:
            move_num += 1
        
        c_dir = (c_dir + 1) % 4
    mode["center_start"].extend([c_dir] * (N-1))

    # (0, 0)에서 시작
    c_dir = 2
    move_num = N-1
    cx, cy = N-1, 0
    mode["zero_start"].extend([c_dir] * move_num)
    while (cx, cy) != (N//2-1, N//2):
        c_dir = (c_dir + 3) % 4

        for _ in range(move_num):
            dx, dy = directions[c_dir]
            nx, ny = cx + dx, cy + dy
            
            mode["zero_start"].append(c_dir)
            cx, cy = nx, ny

        if c_dir % 2 == 0:
            move_num -= 1
    # 마지막 한 칸 아래
    mode["zero_start"].append(2)
    return mode

def is_range(i, j):
    return 0 <= i < N and 0 <= j < N

def runaway():
    # 도망 규칙
    # 1. 현재 바라보고 있는 방향으로 1칸(격자 벗어나지 않고)
    # 2. 움직이려는 칸에 술래가 있는 경우면 움직이지 않는다
    # 3. 술래가 있지않다면 해당 칸으로 이동(나무가 있어도 됨)
    # 4. 현재 바라보고 있는 방향으로 1칸 움직인다고 했을 때 격자를 벗어하는 경우
    #    방향을 반대로 틀고, 그 방향으로 1칸 움직인다 했을 때 해당 위치에 술래가 없다면 1칸 이동

    # 도망자가 움직일 때, 현재 술래와의 거리가 3 이하인 도망자만 움직임(거리 : 맨해튼 거리)

    new_run = [[] for _ in range(N)]

    for i in range(N):
        for j in range(N):
            new_run[i].append([])

    for i in range(N):
        for j in range(N):
            for d in run[i][j]:
                # 거리가 3 초과면 움직이지 않는다
                if abs(i - si) + abs(j - sj) > 3:
                    new_run[i][j].append(d)
                    continue

                di, dj = directions[d]
                ni, nj = i + di, j + dj
                if is_range(ni, nj):
                    # 술래 없을 때
                    if (ni, nj) != (si, sj):
                        new_run[ni][nj].append(d)
                    # 술래가 있으면 움직이지 않는다
                    else:
                        new_run[i][j].append(d)
                else:
                    # 격자 밖 -> 방향 반대로
                    d = (d + 2) % 4
                    di, dj = directions[d]
                    ni, nj = i + di, j + dj
                    if is_range(ni, nj) and (ni, nj) != (si, sj):
                        new_run[ni][nj].append(d)
                    # 술래가 있다면 움직이지 않는다
                    else:
                        new_run[i][j].append(d)
    return new_run


curr_idx = 0
curr_mode = "center_start"

def move_s():
    # 술래는 1번의 턴 동안 한칸 이동
    # 이때, 이동 후의 위치가 이동방향이 틀어지는 지점이라면, 방향을 바로 틀어줌
    # 만약. 이동을 통해 양끝에 해당 하는 위치인 (0, 0) 또는 정 중앙이여도 바로 방향을 틀어줘야함
    global s_dir, si, sj, curr_mode, curr_idx

    c_dir = mode[curr_mode][curr_idx]

    di, dj = directions[c_dir]
    si, sj = si + di, sj + dj
    curr_idx += 1


    if curr_idx == len(mode[curr_mode]):
        curr_mode = "center_start" if curr_mode == "zero_start" else "zero_start"
        curr_idx = 0
        s_dir = mode[curr_mode][0]
    else:
        s_dir = mode[curr_mode][curr_idx]

def catch_run():
    # 이동 직후, 수래는 턴을 넘기기 전에 시야 내에 있는 도망자를 잡음
    # 술래의 시야는 현재 바라보고 있는 방향을 기준으로 현재 칸을 포함한 총 3칸
    # 이때, 만약 나무가 놓여져있다면 해당 칸(그 뒤에 있는 도망자는 아님)에 있는 도망자는 가려져 보이지 않는다

    # 잡힌 도망자는 사라지게 되며, 술래는 현재 턴을 t번째 턴이라고 했을 때, (t * 현재 턴에 잡힌 도망자의 수) 만큼 점수를 얻는다
    
    # s_dir : 술래가 바라보는 방향
    
    # 현재 술래 칸
    temp_si, temp_sj = si, sj
    cnt = 0
    if tree[si][sj] == False and tree[si][sj] == False and run[si][sj]:
        cnt += len(run[si][sj])
    run[si][sj] = []
    
    # 술래가 바라보는 방향 2칸
    for _ in range(2):
        temp_si, temp_sj = temp_si + directions[s_dir][0], temp_sj + directions[s_dir][1]
        # 격자 안, 나무 x, 도망자 있을 때
        if is_range(temp_si, temp_sj) and tree[temp_si][temp_sj] == False and run[temp_si][temp_sj]:
            cnt += len(run[temp_si][temp_sj])
            run[temp_si][temp_sj] = []

    return cnt
    
    # 이걸로 바꾸니 성공

    temp_si, temp_sj = si, sj
    cnt = 0

    for _ in range(3):
        if not is_range(temp_si, temp_sj):
            break

        if not tree[temp_si][temp_sj]:
            cnt += len(run[temp_si][temp_sj])
            run[temp_si][temp_sj] = []
        temp_si += directions[s_dir][0]
        temp_sj += directions[s_dir][1]
    
    return cnt
    



res = 0
mode = make_mode()

for turn in range(1, K+1):
    # 도망자 이동
    run = runaway()

    # 술래 이동
    move_s()

    # 도망자 잡기
    run_cnt = catch_run()

    res += turn * run_cnt
print(res)