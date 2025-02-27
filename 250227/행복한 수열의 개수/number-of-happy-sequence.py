from collections import defaultdict
n, m = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]

# Please write your code here.
# 각 행, 열에서 연속해서 M개 이상의 동일한 원소
res = 0
if n == 1:
    res = 2
else:

    for i in range(n):
        prev = grid[i][0]
        count = 1
        for j in range(1, n):     

            if prev == grid[i][j]:
                count += 1
            else:
                prev = grid[i][j]
                count = 1

            if count >= m:
                res += 1
                break


    for j in range(n):
        prev = grid[0][j]
        count = 1
        for i in range(1, n):
            if prev == grid[i][j]:
                count += 1
            else:
                prev = grid[i][j]
                count = 1
            if count >= m:
                res += 1
                break

print(res)