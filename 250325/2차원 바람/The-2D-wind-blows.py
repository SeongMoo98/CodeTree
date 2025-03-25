# N x M 행렬에 Q번의 바람이 분다

# 특정 직사각형 영역에 경계에 있는 숫자들을 시계방향으로 한칸씩 shift
# 해당 직사각형 내 영역에 있는 값들을 각각 자신의 위치를 기준으로
# 자신과 인접한 원소들의 평균값으로 바꾼다(버림)
# 현재 칸에 적혀있는 숫자 + 인접한 곳에 적혀있는 숫자들의 평균(상하좌우)

N, M, Q = map(int, input().split())

arr = [list(map(int,input().split())) for _ in range(N)]
d = [(0, 1), (0, -1), (1, 0), (-1, 0)]

for _ in range(Q):
    # (r1, c1) : 좌 상단
    # (r2, c2) : 우 하단
    r1, c1, r2, c2 = map(lambda x : int(x)-1, input().split())
    
    # 시계방향 회전
    moving_idx = []
    moving_num = []
    # 가로
    for j in range(c1, c2+1):
        moving_idx.append((r1, j))
        moving_num.append(arr[r1][j])
    for i in range(r1+1, r2):
        moving_idx.append((i, c2))
        moving_num.append(arr[i][c2])
    for j in range(c2, c1-1, -1):
        moving_idx.append((r2, j))
        moving_num.append(arr[r2][j])
    for i in range(r2-1, r1,-1):
        moving_idx.append((i, c1))
        moving_num.append(arr[i][c1])

    temp = moving_num[-1]
    moving_num[1:] = moving_num[0:len(moving_num)-1]
    moving_num[0] = temp


    for idx, (i, j) in enumerate(moving_idx):    
        arr[i][j] = moving_num[idx]
            
    new_arr = arr.copy()
    # 평균 구하기
    for i in range(r1, r2+1):
        for j in range(c1, c2+1):
            temp = [arr[i][j]]
            for di, dj in d:
                ni, nj = i + di, j + dj
                if 0 <= ni < N and 0 <= nj < M:
                    temp.append(arr[ni][nj])
            new_arr[i][j] = int(sum(temp)/len(temp))
        
    for i in range(N):
        for j in range(M):
            print(new_arr[i][j], end=' ')
        print()

