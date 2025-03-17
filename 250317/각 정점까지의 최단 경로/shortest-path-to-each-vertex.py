from collections import defaultdict
import heapq

# N개의 정점과 M개의 간선으로 구성된 무방향 그래프
N, M = map(int, input().split())

# K번 정점에서 다른 모든정점으로 가는 최단경로
K = int(input())

graph = defaultdict(list)
for _ in range(M):
    u, v, c = map(int, input().split())
    graph[u].append((v, c))
    graph[v].append((u, c))

INF = float("inf")
def dijkstra(graph, start):
    distances = [INF] * (N+1)
    pq = []

    heapq.heappush(pq, (0, start))
    distances[start] = 0

    while pq:
        curr_dist, curr_node = heapq.heappop(pq)

        if distances[curr_node] < curr_dist:
            continue

        for next_node, dist in graph[curr_node]:
            next_dist = curr_dist + dist
            if distances[next_node] > next_dist:
                distances[next_node] = next_dist
                heapq.heappush(pq, (next_dist, next_node))
    return distances
distances = dijkstra(graph, K)


[print(-1) if distances[i]==INF else print(distances[i]) for i in range(1, N+1)]