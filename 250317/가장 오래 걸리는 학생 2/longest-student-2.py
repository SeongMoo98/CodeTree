# 다익스트라 : 특정 Node에서 다른 모든 Node까지의 최단거리
# 그렇다면 반대로 모든 정점으로부터 특정 도착점까지의 최단거리?
# 모든 간선을 뒤집은 뒤, 특정 정점에서 다른 모든 정점까지 가는 최단거리를 구하면 된다.
# ==> 다익스트라랑 같은 시간복잡도로 구할 수 있다

from collections import defaultdict
import heapq

# 1~N-1은 학생이 살고있고, N은 학교
# Directed Graph
N, M = map(int, input().split())

# 각 학생은 등교시 최단거리로 학교로 이동
# 이때, 학교를 등교하는데 가장 오래걸리는 학생의 소요시간(거리 1 = 1초의 시간)

graph = defaultdict(list)
reversed_graph = defaultdict(list)
for _ in range(M):
    u, v, d = map(int, input().split())
    # 일반 다익스트라
    graph[u].append((v, d))
    # 역 그래프
    reversed_graph[v].append((u, d))

INF = float('inf')

distances = [INF] * (N+1)

def dijkstra(graph, start):
    pq = []

    heapq.heappush(pq, (0, start))
    distances[start] = 0

    while pq:
        # 현재 최소거리가 정해진 Node
        curr_dist, curr_node = heapq.heappop(pq)

        if distances[curr_node] < curr_dist:
            continue

        for next_node, dist in graph[curr_node]:
            # 현재 최소거리 + curr -> next
            next_dist = distances[curr_node] + dist
            if distances[next_node] > next_dist:
                distances[next_node] = next_dist
                heapq.heappush(pq, (next_dist, next_node))

    return distances

# 역그래프에서 N번 Node(학교)에서 출발
# 이 때의 각 Node별 최단거리
# ==> 모든 학생들의 학교까지의 최단거리
distances = dijkstra(reversed_graph, N)

print(max(distances[1:]))



