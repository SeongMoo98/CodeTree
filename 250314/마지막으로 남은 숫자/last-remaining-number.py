# N개의 수가 주어졌을 때 가장 큰 수 2개를 뽑아 제거하고 두 수의 차이에 해당하는 수를 다시 집어넣기
# 이를 2개 이상의 수가 남아있는 한 계속 반복
# 만약, 뽑은 2개의 수가 동일하하면, 차가 0이기 때문에 새롭게 집어넣지 않는다
# 이 과정을 진행한 이후 마지막으로 남게되는 수를 구하라

import heapq
N = int(input())
nums = list(map(int, input().split()))
nums = [-num for num in nums]
heapq.heapify(nums)

while len(nums) >= 2:
    num1 = heapq.heappop(nums)
    num2 = heapq.heappop(nums)

    sub = abs(num1 - num2)
    if sub != 0:
        heapq.heappush(nums, -sub)

if nums:
    print(-nums[0])
else:
    print(-1)
