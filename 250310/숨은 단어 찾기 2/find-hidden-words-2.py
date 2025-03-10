N, M = map(int, input().split())
arr = [input() for _ in range(N)]

# Please write your code here.

# N x M 문자열
# 가로, 세로, 대각선 방향으로 방향을 틀지않고 나오는 LEE의 갯수

def is_LEE(ci, cj):
    # 상, 하, 좌, 우, 좌상, 좌하, 우하, 우상
    d = [
            [(-1, 0), (1, 0)],      # 상, 하
            [(0, -1), (0, 1)],      # 좌, 우
            [(-1, -1), (1, 1)],     # 좌상, 우하
            [(1, -1), (-1, 1)]      # 좌하, 우상
        ]
    count = 0
    for direc in d:
        ni1, nj1 = ci + direc[0][0], cj + direc[0][1]
        ni2, nj2 = ci + direc[1][0], cj + direc[1][1]
        if (0 <= ni1 < N and 0 <= nj1 < M) and (0 <= ni2 < N and 0 <= nj2 < M):
            if (arr[ni1][nj1] == "E" and arr[ni2][nj2] == "L") or (arr[ni1][nj1] == "L" and arr[ni2][nj2] == "E"):
                count += 1 
    return count




count = 0 
for i in range(N):
    for j in range(M):
        if arr[i][j] == "E":
            count += is_LEE(i, j)
print(count)