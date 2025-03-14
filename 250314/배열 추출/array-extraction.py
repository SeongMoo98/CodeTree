# 1. x가 0이 아닌 자연수라면 x를 배열에 삽입
# 2. x가 0이면 배열에서 가장 큰 값을 출력하고 그 값을 제거

import heapq

N = int(input())
pq = []

heapq.heapify(pq)

for _ in range(N):
    x = int(input())
    if x == 0:
        if pq:
            print(-heapq.heappop(pq))
        else:
            print(0)
    else:
        heapq.heappush(pq, -x)

