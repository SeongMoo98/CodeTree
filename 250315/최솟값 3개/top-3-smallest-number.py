import heapq
N = int(input())

nums = list(map(int, input().split()))

# N개의 수가 하나씩 주어질때, 지금까지 주어진 숫자들 중 가장 작은 3개의 곱을 출력
# 주어진 수가 3개가 되지 않는다면 -1 출력
pq = []

for i in range(N):
    temp = 0
    if i < 2:
        heapq.heappush(pq, -nums[i])
        print(-1)
    elif i == 2:
        heapq.heappush(pq, -nums[i])
        res = 1
        for j in range(3):
            res *= -pq[j]
        print(res)
    else:
        # 3개의 smallest의 max값보다 작다면면
        if nums[i] < -pq[0]:
            heapq.heappop(pq)
            heapq.heappush(pq, -nums[i])
            
        res = 1
        for j in range(3):
            res *= -pq[j]
        print(res)