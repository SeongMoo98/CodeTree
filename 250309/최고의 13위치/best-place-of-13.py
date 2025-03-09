n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]

# Please write your code here.

for i in range(n):
    count = grid[i][0:3].count(1)
    for j in range(n-3):
        count = max(count, grid[i][j:j+3])

print(count)
