# 겹쳐지지 않는 두 직사각형

# N x M 크기의 Matrix
# 영역 안에서 서로 겹치지 않게 두 직사각형을 적절히 잡아,
# 두 직사각형 안에 적힌 숫자들의 총 합을 최대로 만들기
# (경계는 닿아도 된다)

N, M = map(int, input().split())
# N x M 격자
# -1000 <= 정수 값 <= 1000
matrix = [list(map(int, input().split())) for _ in range(N)]

def make_square(ci, cj, N, M, height, length):
    square = []
    for h in range(height+1):
        for l in range(length+1):
            ni, nj = ci + h, cj + l
            if 0 <= ni < N and 0 <= nj < M:
                square.append((ni, nj))
            else:
                return []
    return square

def get_sum(square):
    return sum([matrix[i][j] for i, j in square])

res = -float('inf')
for i in range(N):
    for j in range(M):
        for height in range(N):
            for length in range(M):
                square1 = make_square(i, j, N, M, height, length)
                if square1 == []:
                    continue

                for l in range(N):
                    for m in range(M):
                        for height in range(N):
                            for length in range(M):
                                square2 = make_square(l, m, N, M, height, length)
                                if square2 == []:
                                    continue

                                for ci, cj in square2:
                                    if (ci, cj) in square1:
                                        break
                                else:
                                    res = max(res, get_sum(square1) + get_sum(square2))
                

print(res)