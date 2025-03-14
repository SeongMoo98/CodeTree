N = int(input())

matrix = [list(map(int, input().split())) for _ in range(N)]

dp = [[0] * N for _ in range(N)]

dp[0][N-1] = matrix[0][N-1]
for i in range(1, N):
    dp[i][N-1] = dp[i-1][N-1] + matrix[i][N-1]


for j in range(N-2, -1, -1):
    dp[0][j] = dp[0][j+1] + matrix[0][j]

for i in range(1, N):
    for j in range(N-2, -1, -1):
        dp[i][j] = min(dp[i][j+1] + matrix[i][j], dp[i-1][j] + matrix[i][j])
print(dp[N-1][0])