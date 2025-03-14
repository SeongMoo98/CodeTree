# 2 x N 크기의 사각형을 1 x 2, 2 x 1 크기의 사각형으로 채우는 방법의 수

N = int(input())

dp = [0] * (N+1)

dp[1], dp[2], dp[3] = 1, 2, 3
for i in range(4, N+1):
    dp[i] = dp[i-1] + dp[i-2]
    
print(dp)