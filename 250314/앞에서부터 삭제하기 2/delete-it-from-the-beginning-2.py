# N 개의 정수
# 앞에서부터 K개를 삭제하고 난 후, 남아있는 수 중 가장 작은 숫자를 제외한 평균을 구하고
# 이 평균값이 최대가 될때의 값을 구하여라
import heapq

N = int(input())
nums = list(map(int, input().split()))

nums = nums[::-1]

max_avg = -1

for k in range(1, N-2):
    nums.pop()
    num_temp = nums.copy()
    heapq.heapify(num_temp)
    heapq.heappop(num_temp)

    max_avg = max(max_avg, sum(num_temp) / len(num_temp))    
    

print(f"{max_avg:.2f}")
# print("{:.2f}".format(max_avg))