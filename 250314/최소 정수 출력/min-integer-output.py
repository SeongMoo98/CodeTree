# 1. 입력이 자연수 x 라면 배열에 x 추가
# 2. 입력이 0이라면 배열에서 가장 작은 값을 출력하고, 그 값을 배열에서 제거
import heapq

N = int(input())
pq = []
heapq.heapify(pq)

for _ in range(N):
    num = int(input())
    if num == 0:
        if pq:
            print(heapq.heapq.heappop(pq))
        else:
            print(0)

    else:
        heapq.heappush(pq, num)