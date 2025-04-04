# N x M 크기의 Matrix

# 이 영역 안에서 가능한 양수 직사각형 중 최대 크기를 구하여 한다.
# (직사각형 내 모든 숫자들이 양수)
# 최대 크기의 양수 직사각형을 찾아라(넓이)

N, M = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(N)]


def make_square(ci, cj, height, length):

    for h in range(height+1):
        for l in range(length+1):
            ni, nj = ci + h, cj + l
            if 0 <= ni < N and 0 <= nj < M:
                if matrix[ni][nj] > 0:
                    continue
                else:
                    return -1, -1
    return height + 1, length + 1

res = 0
for i in range(N):
    for j in range(M):
        for height in range(N):
            for length in range(M):
                res_h, res_l = make_square(i, j, height, length)
                if res_h != -1 and res_l != -1:
                    res = max(res, res_h*res_l)

print(res if res !=0 else -1)