# N개의 구역(원형모양으로 순서대로 번호가 있다.)

# 1 -> 2 -> 3 ... -> N -> 1 ...
# 붙어있는 구역으로 이동 가능

# M개의 구간에서 공사
# 1번, 2번 구역에서 공사를 하면 이동 불가

# 건물 중앙에는 모든 구역으로 이동할 수 있기때문에, 길이 막혀있다면 중앙으로 이동 후
# 이동 가능
# 특정 구역 -> 중앙 : 통행권 필요
# 가진 비용 K, 통행권 비용 주어짐

# 이 때, K원의 비용으로 적절히 통행권을 샀을 때, 모든 구역으로 이동할 수 있는지 판단하여라


from collections import defaultdict
import heapq

N, M, K = map(int, input().split())

# 중앙에서 각 지점으로 이동하기 위한 비용
costs = [0] + list(map(int, input().split()))
graph = defaultdict(list)
visited = [False] *(N+1)
# 공사 정보
info = []
for _ in range(M):
    a, b = map(int, input().split())
    info.append((a, b))

for i in range(1, N+1):
    # 공사중인 지점
    if (i, i+1) in info:
        graph[i].append((costs[i] + costs[i+1], i+1))
        graph[i+1].append((costs[i] + costs[i+1], i))
        continue
    if i == N:
        graph[N].append((0, 1))
        graph[1].append((0, N))
    else:
        graph[i].append((0, i+1))
        graph[i+1].append((0, i))


def prim(graph, start):
    MST, total_weight = [], 0
    pq = []
    visited[start] = True

    for w, v in graph[start]:
        heapq.heappush(pq, (w, start, v))

    while pq:
        w, u, v = heapq.heappop(pq)

        if visited[v] == False:
            visited[v] = True
            MST.append((u, v, w))
            total_weight += w

            for next_weight, next_node in graph[v]:
                if visited[next_node] == False:
                    heapq.heappush(pq, (next_weight, v, next_node))

    return MST, total_weight


MST, total_weight = prim(graph, 1)
if K >= total_weight:
    print(1)
else:
    print(0)