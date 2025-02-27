n, m = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]

# Please write your code here.

def block_sum(i, j):
    temp = []

    # 일자 바
    # 가로
    if j + 2 < m:
        temp.append(sum(grid[i][j:j+3]))
    # 세로
    if i + 2 < n:
        temp.append(sum(grid_temp[j] for grid_temp in grid[i:i+3]))
    
    # ㄱ 바
    if i + 1 < n and j + 1 < m:
        temp.append(sum([grid[i][j], grid[i+1][j], grid[i+1][j+1]]))
        temp.append(sum([grid[i][j], grid[i+1][j], grid[i][j+1]]))
        temp.append(sum([grid[i][j], grid[i][j+1], grid[i+1][j+1]]))
        temp.append(sum([grid[i+1][j+1], grid[i][j+1], grid[i+1][j]]))

    if temp:
        return max(temp)
    else:
        return 0


max_value = 0

for i in range(n):
    for j in range(m):
        max_value = max(max_value, block_sum(i, j)) 

print(max_value)