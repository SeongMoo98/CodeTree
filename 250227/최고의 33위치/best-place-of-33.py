n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]

# Please write your code here.

max_count = 0
for i in range(n-3+1):
    for j in range(n-3+1):
        temp = grid[i:i+3]
        count = 0
        for k in range(3):
            count += temp[k][j:j+3].count(1)
        max_count = max(count, max_count)

    
print(max_count)

