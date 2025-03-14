# 2차원 평면 위에 서로 다른 위치에 놓여있는 N개의 점
# 원점에서 가장 가까운 점을 골라, 해당 x, y값에 2씩 더해주는 작업을 M번 반복
# 이 후 원점에서 가장 가까이 있는 점을 출력

# 원점과 특정 점 (x, y)의 거리는 x + y

# 만약 원점과의 거리가 최소인 점이 여러 개 있다면 x값이 가장 작은 점을, 그래도 여러 개면 y값이 가장 작은 점

N, M = map(int, input().split())

points = [tuple(map(int, input().split())) for _ in range(N)]

points = [ (x + y, x, y) for x, y in points]

import heapq
heapq.heapify(points)

for _ in range(M):
    if points:
        dist, x, y = heapq.heappop(points)
        heapq.heappush(points, (dist+4, x+2, y+2))

print(points[0][1], points[0][2])


