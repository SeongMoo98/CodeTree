# Node A, B, C가 주어질때, 특정 Node를 잘 잡아 
# A, B, C 중 가장 가까운 정점까지의 거리가 최대가 되도록 하여라
from collections import defaultdict
import heapq

N, M = map(int, input().split())

starts = list(map(int, input().split()))

graph = defaultdict(list)
for _ in range(M):
    u, v, d = map(int, input().split())
    graph[u].append((v, d))
    graph[v].append((u, d))

# N이 100,000개라 A, B, C를 제외한 Node들로 다익스트라를 적용하는 것은 무리
# A, B, C를 시작으로 하는 다익스트라 3번

INF = float('inf')
def dijkstra(graph, start):
    pq = []
    distances = [INF] * (N+1)

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

    return distances

starts_dist = []
for start in starts:
    starts_dist.append(dijkstra(graph, start))

res = -1
for i in range(1, N+1):
    # A, B, C 이면 Pass
    if i in starts:
        continue
    
    # A -> i, B -> i, C -> i 들 중 최솟값
    # 그 중 최대값
    res = max(res, min(starts_dist[0][i], starts_dist[1][i], starts_dist[2][i]))

print(res)

