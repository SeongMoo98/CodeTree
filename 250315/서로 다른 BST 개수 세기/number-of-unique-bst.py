# 1 ~ N 까지의 숫자들을 단 한번씩 써서 만들수 있는 서로 다른 N개의 이진트리 개수

N = int(input())


dp = [0]*(N+1)
# 0 : 아무것도 없는 상태가 1로 취급
dp[0], dp[1], dp[2] = 1, 1, 2

# ex) N = 4
# root 1 : 오른쪽에 2,3,4
# root 2 : 왼쪽에 1, 오른쪽에 3,4
# root 3 : 왼쪽에 1, 2, 오른쪽에 4
# root 4 : 오른쪽에 1,2,3

# ==> dp[0]*dp[3], dp[1]*dp[2], dp[2]*dp[1], dp[3],dp[0]

for i in range(3, N+1):
    for j in range(i):
        dp[i] += dp[j] * dp[i-j-1]

print(dp[N])