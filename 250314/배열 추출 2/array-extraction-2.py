# 1. x가 0이 아니라면 x를 배열에 추가
# 2. x가 0이라면, 배열에서 절댓값이 가장 작은 정수를 출력 후 제거
# 3. 절대값이 가장 작은 수가 여러 개라면, 그 중 작은 수를 선택

import heapq

N = int(input())
arr = []
heapq.heapify(arr)

# (절대값, 원래 값)
for _ in range(N):
    x = int(input())
    if x != 0:
        heapq.heappush(arr, (abs(x), x))
    else :
        if arr:
            abs_x, x = heapq.heappop(arr)
            print(x)
        else:
            print(0)

