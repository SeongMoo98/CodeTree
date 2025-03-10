board = [list(map(int, input().split())) for _ in range(19)]

# Please write your code here.
# 입력으로 바둑판의 상태가 주어지면
# 검은색 바둑알이 이겼는지, 흰색 바둑알이 이겼는지, 아직 승부가 나지 않았는지 판다
# 검은 바둑알 : 1, 흰색 바둑알 : 2, 알 X : 0

def check_win(color, ci, cj):
    steps = []
    # 세로
    if ci - 2 >= 0 and ci + 2 < 19:
        count = 0
        for i in range(ci-2, ci + 3):
            if board[i][cj] == color:
                count += 1
        steps.append(count)
    # 가로 
    if cj - 2 >= 0 and cj + 2 < 19:
        count = 0
        for j in range(cj-2, cj+3):
            if board[ci][j] == color:
                count += 1
        steps.append(count)
    
    if ci - 2 >= 0 and ci + 2 < 19 and cj - 2 >= 0 and cj + 2 < 19:
        # 왼쪽 대각
        count = 0
        for step in range(-2, 3):
            if board[ci+step][cj+step] == color:
                count += 1
        steps.append(count)
        # 오른쪽 대각
        count = 0
        for step in range(-2, 3):
            if board[ci+step][cj-step] == color:
                count += 1
        steps.append(count)

    if 5 in steps:
        return True


for i in range(19):
    for j in range(19):
        if board[i][j] == 1 or board[i][j] == 2:
            if check_win(board[i][j], i, j):
                print(board[i][j])
                print(i+1, j+1)