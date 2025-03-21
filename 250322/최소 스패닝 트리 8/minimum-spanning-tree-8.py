# MST 구하기

from collections import defaultdict
import heapq

N, M = map(int, input().split())

graph = defaultdict(list)

for _ in range(M):
    u, v, w = map(int, input().split())
    graph[u].append((w, v))
    graph[v].append((w, u))

def prim(graph, start):
    MST, total_weight = [], 0
    pq = []
    visited = [start]
    
    for w, v in graph[start]:
        heapq.heappush(pq, (w, start, v))

    while pq:
        w, u, v = heapq.heappop(pq)

        if v not in visited:
            MST.append((u, v, w))
            total_weight += w
            visited.append(v)

            for next_dist, next_node in graph[v]:
                if next_node not in visited:
                    heapq.heappush(pq, (next_dist, v, next_node))

    return MST, total_weight

MST, total_weight = prim(graph, 1)
print(total_weight)
