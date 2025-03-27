# (1, 1)에서 시작하여, 오른쪽 혹은 밑으로만 이동하여 (N, N)으로 갈때,
# 거쳐간 위치에 적혀있는 숫자들 중 최솟값을 최대로 하여라
INF = float('inf')

N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]

dp = [[0] * N for _ in range(N)]
dp[0][0] = arr[0][0]

for i in range(1, N):
    dp[i][0] = min(dp[i-1][0], arr[i][0])
for j in range(1, N):
    dp[0][j] = min(dp[0][j-1], arr[0][j])

for i in range(1, N):
    for j in range(1, N):
        dp[i][j] = max(min(dp[i-1][j], arr[i][j]), min(dp[i][j-1], arr[i][j]))
print(dp[N-1][N-1])


