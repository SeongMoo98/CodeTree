# 특정 시작점에서 특정 도착점으로 최단거리로 이동하기위한 경로 구하기
# path 배열을 만들어 distances[i]가 dist[curr_node] + graph[curr_node][i]로 
# 갱신되는 순간 path[i]에 curr_node 넣어주기
# ==> path[i]에 i번째 Node에서 최단거리로 도달하기 위한 바로 직전의 Node 번호가 적힌다


# 점정 A에서 B 까지의 최단거리와 그때의 경로를 구하여라
# Undirected Graph

from collections import defaultdict
import heapq

N, M = map(int, input().split())

graph = defaultdict(list)

for _ in range(M):
    u, v, c = map(int, input().split())
    graph[u].append((v, c))
    graph[v].append((u, c))

A, B = map(int, input().split())

INF = float('inf')
distances = [INF] * (N+1)
path = [-1] * (N+1)

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
                # distances가 갱신
                # next_node는 curr_node에서 왔다
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


