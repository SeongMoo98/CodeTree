# N x N 격자판
# 특정 열을 선택하면, 해당 열에 숫자가 적혀있는 위치 중 가장 위에 있는 칸을 중심으로 
# 십자 모양으로 폭탄이 터짐

# 십자 모양의 크기는 선택된 숫자에 비례하여 커짐

# 폭탄이 터지고 중력이 작용한다


N, M = map(int, input().split())

arr = [list(map(int, input().split())) for _ in range(N)]

cols = [int(input())-1 for _ in range(M)]

def bomb_size(size, ci, cj):
    bomb_idx = [(ci, cj)]
    # arr[i][j]에 비례하는 폭탄 코기
    
    for s in range(1, size):    
        if 0 <= ci + s < N and 0 <= cj < N:
            bomb_idx.append((ci + s, cj))
        if 0 <= ci - s < N and 0 <= cj < N:
            bomb_idx.append((ci - s, cj))
        if 0 <= ci < N and 0 <= cj + s < N:
            bomb_idx.append((ci, cj + s))
        if 0 <= ci < N and 0 <= cj - s < N:
            bomb_idx.append((ci, cj - s))
    return bomb_idx



for col in cols:
    new_arr = [[0] * N for _ in range(N)]   
    for i in range(N):
        if arr[i][col] != 0:
            bomb_idx = bomb_size(arr[i][col], i, col)
            break
    else:
        continue
    # 폭탄 터트릴 곳이 있을 때
    if bomb_idx:
        # 폭탄 터트리기
        for ni, nj in bomb_idx:
            arr[ni][nj] = 0

        # 밑으로 중력
        for j in range(N):
            temp = []
            for i in range(N-1, -1, -1):
                if arr[i][j] != 0:
                    temp.append(arr[i][j])
            
            curr_idx = N-1
            for i in range(len(temp)):
                new_arr[curr_idx][j] = temp[i]
                curr_idx -= 1 

    for i in range(N):
        for j in range(N):
            arr[i][j] = new_arr[i][j]

for i in range(N):
    for j in range(N):
        print(arr[i][j], end=' ')
    print()
            


