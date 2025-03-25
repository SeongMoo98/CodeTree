# 0, 1로 구성된 N x N 격자

# 1은 해당 위치에 폭탄이 놓임

# 1이 적인 위치에 3가지 폭탄을 선택하여 초토화시킬 지역의 수를 최대화

# 초기 격자판의 상태와 폭탄을 놓아야 할 위치들이 주어졌을 때, 
# 가장 많이 초토화 시킬 수 있는 영역의 수 

N = int(input())

arr = [list(map(int, input().split())) for _ in range(N)]

bombs = []

for i in range(N):
    for j in range(N):
        if arr[i][j] == 1:
            bombs.append((i, j))

num_of_bomb = len(bombs)
max_bomb = 0
d = {
    1: [(-2, 0), (-1, 0), (0, 0), (1, 0), (2, 0)],
    2: [(1, 0), (-1, 0), (0, 0), (0, 1), (0, -1)],
    3: [(1, -1), (1, 1), (0, 0), (-1, -1), (-1, 1)]
}
def backtrack(ans):
    global num_of_bomb, max_bomb
    if len(ans) == num_of_bomb:
        res = set()    

        for bomb_type, (i, j) in zip(ans, bombs):
            for di, dj in d[bomb_type]:
                ni, nj = i + di, j + dj
                if 0 <= ni < N and 0 <= nj < N:
                    res.add((ni,  nj))
        max_bomb = max(max_bomb, len(res))
        return 

    
    for i in range(1, 4):
        ans.append(i)
        backtrack(ans)
        ans.pop()

backtrack([])
print(max_bomb)