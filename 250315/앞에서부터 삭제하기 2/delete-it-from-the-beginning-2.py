# N 개의 정수
# 앞에서부터 K개를 삭제하고 난 후, 남아있는 수 중 가장 작은 숫자를 제외한 평균을 구하고
# 이 평균값이 최대가 될때의 값을 구하여라
import heapq
from collections import deque

N = int(input())
nums = list(map(int, input().split()))

max_avg = -1

nums = deque(nums)
for k in range(1, N-1):
    nums.popleft()
    max_avg = max(max_avg, (sum(nums)-min(nums)) / len(nums)-1 )
print(f"{max_avg:.2f}")
# print("{:.2f}".format(max_avg))
