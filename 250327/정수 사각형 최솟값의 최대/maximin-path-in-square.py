# (1, 1)에서 시작하여, 오른쪽 혹은 밑으로만 이동하여 (N, N)으로 갈때,
# 거쳐간 위치에 적혀있는 숫자들 중 최솟값을 최대로 하여라
INF = float('inf')

N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]

dp =[[INF] * (N+1)] + [[INF] + [0] * N for _ in range(N)]

dp[1][1] = arr[0][0]

for i in range(1, N+1):
    for j in range(1, N+1):
        dp[i][j] = min(dp[i-1][j], dp[i][j-1], arr[i-1][j-1])

print(max(dp[N-1][N], dp[N][N-1], dp[N-1][N-1]))


