# N 개의 정수
# 앞에서부터 K개를 삭제하고 난 후, 남아있는 수 중 가장 작은 숫자를 제외한 평균을 구하고
# 이 평균값이 최대가 될때의 값을 구하여라
import heapq

N = int(input())
nums = list(map(int, input().split()))
heapq.heapify(nums)

max_avg = -1

# K는 1에서 N-2
for k in range(1, N-1):
    # k개 삭제
    k_sum = sum(heapq.nlargest(k, nums))
    # 제일 작은 수
    min_val = nums[0]

    avg = (sum(nums) - k_sum - min_val) / (N - k -1)
    max_avg = max(max_avg, avg)


print(f"{max_avg:.2f}")
print("{.2f}".format(max_avg))
print(round(max_avg, 2))