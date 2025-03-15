N = int(input())

MOD = 10007
MAX_N = 1000
dp = [0] * (MAX_N + 1)

dp[0], dp[1], dp[2] = 1, 1, 3

for i in range(3, MAX_N):
    dp[i] = (dp[i-1] + 2 * dp[i-2]) % MOD

print(dp[N])