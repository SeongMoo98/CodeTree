# 1 ~ 100 숫자로 이루어진 N x N 격자

# 격자 내에 있는 기울어진 사각형을 살펴보려한다
# 기울어진 사각형
# 격자 내에 있는 한 지점으로부터 대각선으로 움직이며
# 반시계 방향으로 순회했을 때 지나왔던 지점들의 집합
# (격자 밖으로 넘어가서는 안된다)

# 기울어진 직사각형들 중 해당 직사각형을 이루는 지점에 적힌 숫자들의 최대 합

N = int(input())
matrix = [list(map(int, input().split())) for _ in range(N)]

res = 0


def get_sum(ci, cj, len_one, len_two):
    ret = 0
    # 1번
    di, dj = -1, 1
    for one in range(len_one):
        ni, nj = ci + di, cj + dj
        if 0 <= ni < N and 0 <= nj < N:
            ret += matrix[ni][nj]
            ci, cj = ni, nj
        else:
            return 0 
    # 2번
    di, dj = -1, -1
    for one in range(len_two):
        ni, nj = ci + di, cj + dj
        if 0 <= ni < N and 0 <= nj < N:
            ret += matrix[ni][nj]
            ci, cj = ni, nj
        else:
            return 0 

    # 3번
    di, dj = 1, -1
    for one in range(len_one):
        ni, nj = ci + di, cj + dj
        if 0 <= ni < N and 0 <= nj < N:
            ret += matrix[ni][nj]
            ci, cj = ni, nj
        else:
            return 0 

    # 4번
    di, dj = 1, 1
    for one in range(len_two):
        ni, nj = ci + di, cj + dj
        if 0 <= ni < N and 0 <= nj < N:
            ret += matrix[ni][nj]
            ci, cj = ni, nj
        else:
            return 0 
    return ret

# len_one + len_two <= N-1
for len_one in range(1, N-1):
    for len_two in range(1, N-1):
        if len_one + len_two > N-1:
            continue

        for i in range(N):
            for j in range(N):
                diamond_sum = get_sum(i, j, len_one, len_two)
                if diamond_sum != 0:
                    res = max(res, diamond_sum)

print(res)
                
