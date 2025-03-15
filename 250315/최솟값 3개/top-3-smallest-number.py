import heapq
N = int(input())

nums = list(map(int, input().split()))

# N개의 수가 하나씩 주어질때, 지금까지 주어진 숫자들 중 가장 작은 3개의 곱을 출력
# 주어진 수가 3개가 되지 않는다면 -1 출력

for i in range(N):
    if i < 2:
        print(-1)
    else:
        res = 1
        smallest_three = heapq.nsmallest(3, nums[:i+1])
        for j in range(3):
            res *= smallest_three[j]
        print(res)