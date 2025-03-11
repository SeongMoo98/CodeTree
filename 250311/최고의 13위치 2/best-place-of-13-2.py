n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]

# Please write your code here.

# N x N 격자(동전이 있으면 1)
# 1 x 3 크기의 격자 2개를 겹치지 않게 해서 범위 안에 들어있는 동전의 개수를 최대로
# 격자는 세로 1 가로 3

max_count = 0
for i in range(n):
    for j in range(n-2):
        grid1 = arr[i][j:j+3]
        for l in range(n):
            for m in range(n-2):
                if i == l and (j <= m <= j+2 or j <= m+1 <= j+2 or j <= m+2 <= j+2):
                    continue
                grid2 = arr[l][m:m+3]
                max_count = max(max_count, grid1.count(1) + grid2.count(1))

print(max_count)
