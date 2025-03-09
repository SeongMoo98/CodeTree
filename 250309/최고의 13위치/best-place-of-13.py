n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]

# Please write your code here.
count = 0 
for i in range(n):
    count = max(count, grid[i][0:3].count(1))
    for j in range(n-2):
        count = max(count, grid[i][j:j+3].count(1))

print(count)
