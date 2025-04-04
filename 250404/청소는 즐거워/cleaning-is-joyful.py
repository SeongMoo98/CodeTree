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

matrix = [list(map(int, input().split())) for _ in range(N)]

# 0 : 좌 -> 1 : 하 -> 2 : 우 -> 3: 상
dust_ratio={
    0:[ [0, 0, 0.02, 0, 0],
        [0, 0.1, 0.07, 0.01, 0],
        [0.05, 0, 0, 0, 0],
        [0, 0.1, 0.07, 0.01, 0],
        [0, 0, 0.02, 0, 0] ],

    1:[ [0, 0, 0, 0, 0],
        [0, 0.01, 0, 0.01, 0],
        [0.02, 0.07, 0, 0.07, 0.02],
        [0, 0.1, 0, 0.1, 0],
        [0, 0, 0.05, 0, 0] ],

    2:[ [0, 0, 0.02, 0, 0],
        [0, 0.01, 0.07, 0.1, 0],
        [0, 0, 0, 0, 0.05],
        [0, 0.01, 0.07, 0.1, 0],
        [0, 0, 0.02, 0, 0] ],

    3:[ [0, 0, 0.05, 0, 0],
        [0, 0.1, 0, 0.1, 0],
        [0.02, 0.07, 0, 0.07, 0.02],
        [0, 0.01, 0, 0.01, 0],
        [0, 0, 0, 0, 0] ],
}

directions = {
    0 : (0, -1),
    1 : (1, 0),
    2 : (0, 1),
    3 : (-1, 0)
}

ci, cj = N//2, N//2
ei, ej = 0, 0
res = 0
def add_dust(ci, cj, dust):
    global res

    if 0 <= ci < N and 0 <= cj < N:
        matrix[ci][cj] += dust
    else:
        res += dust
    

def move():
    global ci, cj

    ci, cj = ci + directions[move_dir][0], cj + directions[move_dir][1]

    dust_sum = 0
    for i in range(5):
        for j in range(5):
            dust = int(matrix[ci][cj] * dust_ratio[move_dir][i][j])
            add_dust(ci + i -2, cj + j -2 , dust)

            dust_sum += dust

    add_dust(ci + directions[move_dir][0], cj + directions[move_dir][1],
             matrix[ci][cj] - dust_sum)

# 초기 방향, 초기 횟수
move_dir, move_num = 0, 1
while (ci, cj) != (ei, ej):
    for _ in range(move_num):
        move()

        if (ci, cj) == (ei, ej):
            break

    move_dir = (move_dir + 1) % 4

    if move_dir == 0 or move_dir == 2:
        move_num += 1

print(res)