# N개의 정점과 M개의 간선
# A -> B 까지의 최단 거리와 그때의 경로

from collections import defaultdict
import heapq

N, M = map(int, input().split())

graph = defaultdict(list)
INF = float('inf')

distances = [INF] * (N+1)

for _ in range(M):
    u, v, d = map(int, input().split())
    graph[u].append((v, d))
    graph[v].append((u, d))

A, B = map(int, input().split())

path = [0] * (N+1)
def dijkstra(graph, start):
    pq = []
    
    heapq.heappush(pq, (0, start))
    distances[start] = 0
    path[start] = start
    while pq:
        curr_dist, curr_node = heapq.heappop(pq)

        if distances[curr_node] < curr_dist:
            continue 
 
        for next_node, dist in graph[curr_node]:
            next_dist = distances[curr_node] + dist
            if distances[next_node] > next_dist:
                distances[next_node] = next_dist
                path[next_node] = curr_node
                heapq.heappush(pq, (next_dist, next_node))

dijkstra(graph, A)
print(distances[B])
res = [B]
curr = B
while curr != A:
    curr = path[curr]
    res.append(curr)

[print(num, end=' ') for num in res[::-1]]