# 2 x N 크기의 사각형에
# 1 x 2, 2 x 1, 1 x 1 크기의 사각형으로 채우기

N = int(input())

MAX_N = 1000
MOD = 1000000007
dp = [0] * (MAX_N+1)

dp[0], dp[1] = 1, 2

for i in range(2, MAX_N+1):
    dp[i] = (dp[i-1]*2 + dp[i-2]*3) % MOD
    for j in range(i-3, -1, -1):
        dp[i] = (dp[i] + dp[j] * 2) % MOD



print(dp[N])