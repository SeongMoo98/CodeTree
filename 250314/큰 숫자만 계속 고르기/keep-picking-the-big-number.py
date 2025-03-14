import heapq
N, M = map(int, input().split())

# 가장 클 수를 골라 1씩 뺴는 작업을 M번 반복
# 남아 있는 수 중 최댓값 구하기
nums = list(map(int, input().split()))
nums = [-num for num in nums]
# Max Heap
heapq.heapify(nums)

for _ in range(M):
    max_num = -heapq.heappop(nums) 
    heapq.heappush(nums, -(max_num-1))
print(-nums[0])



