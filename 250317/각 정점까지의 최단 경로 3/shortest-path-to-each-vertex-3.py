from collections import defaultdict
import heapq

# Vertex : N, Edge : M
N, M = map(int, input().split())

graph = defaultdict(list)

for _ in range(M):
    u, v, c = map(int, input().split())
    graph[u].append((v, c))

INF = float('inf')
dist = [INF] * (N + 1)
def dijkstra(graph, start_node):
    pq = []
    
    # 현재 dist, Node
    # dist가 작은걸 뽑아야 하기 때문에 dist를 첫번째 원소로
    heapq.heappush(pq, (0, start_node))
    dist[start_node] = 0

    while pq:
        # curr node는 최소길이가 확정된 Node
        curr_dist, curr_node = heapq.heappop(pq)
        
        # 이미 처리된 최단경로보다 긴 경로는 무시
        if dist[curr_node] < curr_dist:
            continue

        # curr_node -> next_node의 거리는 cost
        for next_node, cost in graph[curr_node]:
            next_dist = curr_dist + cost
            if dist[next_node] > next_dist:
                dist[next_node] = next_dist
                heapq.heappush(pq, (dist[curr_node] + cost, next_node)) 

dijkstra(graph, 1)

for i in range(2, N+1):
    print(-1 if dist[i] == INF else dist[i])


