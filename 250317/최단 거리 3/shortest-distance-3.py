from collections import defaultdict
import heapq

N, M = map(int, input().split())

graph = defaultdict(list)
for _ in range(M):
    u, v, d = map(int, input().split())
    graph[u].append((v, d))
    graph[v].append((u, d))

A, B = map(int, input().split())

INF = float('inf')
distances = [INF] * (N+1)

def dijkstra(graph, start):
    pq = []

    heapq.heappush(pq, (0, start))
    distances[start] = 0

    while pq:
        curr_dist, curr_node = heapq.heappop(pq)

        if distances[curr_node] < curr_dist:
            continue

        for next_node, dist in graph[curr_node]:
            next_dist = distances[curr_node] + dist
            if distances[next_node] > next_dist:
                distances[next_node] = next_dist
                heapq.heappush(pq, (next_dist, next_node))

# Start Node를 
dijkstra(graph, A)

print(distances[B])
# 정점 A -> B 까지의 최단거리