from collections import defaultdict
import heapq
# 1 ~ N개의 정점, M개의 Edge
# 그래프에서 MST를 구하여라

N, M = map(int, input().split())

INF = float('inf')
distances = [INF] * (N+1)

graph = defaultdict(list)

for _ in range(M):
    u, v, w = map(int, input().split())
    graph[u].append((w, v))
    graph[v].append((w, u))


def prim(graph, start):
    MST = []
    total_weight = 0
    pq = []
    visited = []

    visited.append(start)

    for w, v in graph[start]:
        heapq.heappush(pq, (w, start, v))

    while pq:
        w, u, v = heapq.heappop(pq)

        if v not in visited:
            visited.append(v)
            MST.append((u, v, w))
            total_weight += w

            for next_weight, next_node in graph[v]:
                if next_node not in visited:
                    heapq.heappush(pq, (next_weight, v, next_node))

    return MST, total_weight

MST, total_weight = prim(graph, 1)

print(total_weight)