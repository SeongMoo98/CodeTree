N = int(input())
matrix = [list(map(int, input().split())) for _ in range(N)]
dp = [[0] * N for _ in range(N)]

for j in range(N):
    dp[0][j] = sum(matrix[0][:j+1])

for i in range(N):
    sub_sum = 0
    for k in range(i+1):
        sub_sum += matrix[k][0]
    dp[i][0] = sub_sum


for i in range(1, N):
    for j in range(1, N):
        dp[i][j] = max(dp[i-1][j-1] + dp[i][j-1], dp[i-1][j-2] + dp[i-1][j])
print(dp[N-1][N-1])
    