# 바닥 먼지 양을 담은 N x N 행렬(N은 홀수)

# 정 가운데부터 시작해서 나선형으로 바닥 청소(좌, 하, 우, 상)
# N이 홀수이기 때문에 항상 왼쪽 위에서 끝남

# 빗자루가 이동할 때마다 빗자루가 이동한 위치의 격자에 있는 먼지가 함께 이동(비율이 있다.)
# 빗자루가 이동한 위치에 있는 먼지는 모두 없어짐
# a%는 curr에 있던 양 - 날아간 먼지양의 비율(비율을 계산하고 소수점 아래 숫자는 버림)

# 정중앙에서 시작하여 좌측 상단까지 도달하는데 겪자 밖으로 떨어진 먼지 양의 총합을 계산

# N : 격자의 크기
# dust = 먼지의 양

N = int(input())

# (i, j)에서 curr : (i, j-1)로 움직일 때
# i, j 기준
browse = [
    ((-1, 0), 0.01),
    ((1, 0), 0.01),    
    ((-2, -1), 0.02),
    ((-1, -1), 0.07),
    ((1, -1), 0.07),
    ((2, -1), 0.02),
    ((-1, -2), 0.1),
    ((1, -2), 0.1),
    ((0, -3), 0.05),
    ((0, -2), -1),
]
        


dust = [list(map(int, input().split())) for _ in range(N)]

res = 0
# 빗자루가 왼쪽으로 움직일 때
def get_dust(ci, cj):
    global res
    if cj == 0:
        return
    
    curr_dust = dust[ci][cj-1]
    # curr은 0
    dust[ci][cj-1] = 0
    dust_sum = 0
    for (di, dj), r in browse:
        ni, nj = ci + di, cj + dj

        move_dust = int(curr_dust * r)

        # 범위 안 먼지
        if 0 <= ni < N and 0 <= nj < N:
            if r > 0:
                dust_sum += move_dust
                dust[ni][nj] += move_dust
            # a % : 나머지
            else:
                move_dust = curr_dust - dust_sum
                dust[ni][nj] += move_dust
        # 범위 밖 먼지
        else:
            if r > 0:
                dust_sum += move_dust
                res += move_dust
            else:
                move_dust = curr_dust - dust_sum
                res += move_dust
            

# 시계 방향 회전전
def rotate():   
    global dust
    dust = list(map(list, zip(*dust[::-1])))

# 나선형 회전
# 좌 1, 하 1, 우 2, 상 2, 좌 3, 하 3, 우 4, 상 4, 마지막 좌 4한번 더
# 즉, N-1번까지 회전


# 좌, 하, 우, 상
dirs = [0, 1, 2, 3]
d = [(0, -1), (1, 0), (0, 1), (-1, 0)]

# (방향, 이동횟수)
move = []
idx = 0
for step in range(1, N):
    for j in range(2):
        move.append((dirs[idx], step))
        idx = (idx + 1) % 4
move.append((0, N-1))
        
# 출발점
si, sj = (N-1)//2, (N-1)//2
ci, cj = si, sj
ei, ej = 0, 0

# 방향, 이동횟수
for move_dir, count in move:
    for _ in range(count):
        di, dj = d[move_dir]
        
        if move_dir == 0:
            get_dust(ci, cj)
        # 하 : 1번 회전
        if move_dir == 1:
            rotate()
            ci, cj = cj, (N-1-ci)

            get_dust(ci, cj)

            for _ in range(3):
                rotate()
                ci, cj = cj, (N-1-ci)
        # 우 : 2번 회전전
        if move_dir==2:
            for _ in range(2):
                rotate()
                ci, cj = cj, (N-1-ci)

            get_dust(ci, cj)

            for _ in range(2):
                rotate()
                ci, cj = cj, (N-1-ci)
        # 상 :3번 회전
        if move_dir == 3:
            for _ in range(3):
                rotate()
                ci, cj = cj, (N-1-ci)
                
            get_dust(ci, cj)

            rotate()
            ci, cj = cj, (N-1-ci)
        
        ci, cj = ci + di, cj + dj
print(res)