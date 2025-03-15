# N 개의 정수
# 앞에서부터 K개를 삭제하고 난 후, 남아있는 수 중 가장 작은 숫자를 제외한 평균을 구하고
# 이 평균값이 최대가 될때의 값을 구하여라
import heapq
from collections import deque

N = int(input())
nums = list(map(int, input().split()))
# 왜 자꾸 nums를 heap으로 만들려고 했을까..!
pq = []
heapq.heappush(pq, nums[N-1])
res_sum = nums[N-1]

max_avg = -1
for i in range(N-2, 0, -1):
    heapq.heappush(pq, nums[i])
    
    res_sum += nums[i]

    min_val = pq[0]

    max_avg = max(max_avg, (res_sum - min_val) / (N- i - 1))

print(f"{max_avg:.2f}")
# print("{:.2f}".format(max_avg))
