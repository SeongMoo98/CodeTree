from collections import defaultdict
import heapq

N, M = map(int, input().split())

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

    # 출발 Vertex에 연결된 Vertex들
    for w, v in graph[start]:
        heapq.heappush(pq, (w, start, v))
    # 시작점을 방문 처리
    visited.append(start)

    while pq:
        w, u, v = heapq.heappop(pq)

        # Weight가 가장 작고, Vertex v를 방문 x일 때
        if v not in visited:
            visited.append(v)
            MST.append((u, v, w))
            total_weight += w

            # Vertex v에 연결된 Vertex 확인
            for next_weight, next_node in graph[v]:
                if next_node not in visited:
                    heapq.heappush(pq, (next_weight, v, next_node))

    return MST, total_weight

MST, total_weight = prim(graph, 1)
print(total_weight)


