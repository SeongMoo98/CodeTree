# N x N 격자판

# 특정위치를 선택하면, 그 위치를 중심으로 십자모양으로 폭탄이 터짐
# 터진 이후에는 중력에 의해 숫자들이 아래로 떨어짐

# 십자 모양의 크기는 선택된 숫자에 비례하여 커짐
# ex) 4 : 상하좌우 3칸

# 폭탄이 터져야하는 범위가 격자 판을 벗어나도 격자안에서만 터짐
# 터진 칸은 0

N = int(input())

arr = [list(map(int, input().split())) for _ in range(N)]

# [r][c]에서 터지는데 해당 칸의 수에 맞는 폭탄 크기
r, c = map(lambda x : int(x)-1, input().split())
size = arr[r][c]

bomb_idx = [(r, c)]
for s in range(1, size):
    if 0 <= r + s < N and 0 <= c < N:
        bomb_idx.append((r+s, c))

    if 0 <= r - s < N and 0 <= c< N:
        bomb_idx.append((r-s, c))

    if 0 <= r < N and 0 <= c + s < N:
        bomb_idx.append((r, c+s))
    
    if 0 <= r  < N and 0 <= c - s < N:
        bomb_idx.append((r, c-s))

# 폭탄 처리
for i in range(N):
    for j in range(N):
        if (i, j) in bomb_idx:
            arr[i][j] = 0
    
temp_arr = [[0] * N for _ in range(N)]

for j in range(N):
    res = []
    for i in range(N-1, -1, -1):
        if arr[i][j] != 0:
            res.append(arr[i][j])
    idx = N-1
    for i in range(len(res)):
        temp_arr[idx-i][j] = res[i]

for i in range(N):
    for j in range(N):
        print(temp_arr[i][j], end=' ')
    print()


    
