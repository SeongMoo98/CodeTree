# N x M 행렬에 Q번의 바람이 분다

# 바람 : 특정 행의 모든 원소를 왼쪽 or 오른쪽으로 전부 한칸씩 민다.

# 바람의 영향을 받아 특정 행의 숫자들이 한칸씩 밀리게되면, 위 아래로도 영향을 미친다.
# 밀리기 시작한 행을 기준으로 위아랴 방향으로 순차적으로 전파

# 전파가 이어질 조건
# 현재 행과 나아가려는 행을 비교했을 때, 단 하나라도 같은 열에 숫자가 적혀있는경우 전파를 이어감
# 같은 숫자가 하나도 존재하지 않거나 끝에 다달았으면 전파 종료
# 현재 행이 밀렸던 방향과 반대방향으로 작용

# 총 Q개의 바람이 거친 후의 상태 출력
N, M, Q = map(int, input().split())

grid = [list(map(int,input().split())) for _ in range(N)]
def wind(row, direction):
    global grid
    # 왼쪽에서 불어온다 : 따라서 오른쪽으로 이동
    if direction == "L":
        temp = grid[row][-1]
        grid[row][1:] = grid[row][0:M-1]
        grid[row][0] = temp

    if direction == "R":
        temp = grid[row][0]
        grid[row][0:M-1] = grid[row][1:]
        grid[row][-1] = temp
    
def propagation_up(row, direction):
    global grid
    ci = row
    while True:
        ni = ci - 1
        if ni < 0:
            break

        for j in range(M):
            if grid[ci][j] == grid[ni][j]:
                break
        # 같은게 하나도 없으면 끝
        else:
            break
        direction = "L" if direction == "R" else "R"
        wind(ni, direction)
        ci = ni

def propagation_down(row, direction):
    global grid
    ci = row
    while True:
        ni = ci + 1
        if ni >= N:
            break

        for j in range(M):
            if grid[ci][j] == grid[ni][j]:
                break
        # 같은게 하나도 없으면 끝
        else:
            break
        direction = "L" if direction == "R" else "R"
        wind(ni, direction)
        ci = ni


# 위에서부터 1 ~ N
for _ in range(Q):
    row, direction = input().split()
    row = int(row)-1

    wind(row, direction)
    propagation_up(row, direction)
    propagation_down(row, direction)

for i in range(N):
    for j in range(M):
        print(grid[i][j], end=' ')
    print()