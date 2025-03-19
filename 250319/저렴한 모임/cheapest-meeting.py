# N개의 Vertex, M개의 Edge, Undirected Graph

# A : vertex v1에처 출발하여 vertex e로 이동
# B : vertex v2에서 출발하여 vertex e로 이동

# 각 edge 마다 택시 비가 있다

# 단, A와 B가 특점 지점에서 만나 동일한 택시를 타고 함께 이동 가능
# 동일한 Edge를 여러번 지나는 것도 가능(추가 비용 발생)

# 이때, 두사람이 정점 e에 도착하기 위해 지불해야 하는 비용 중 최소 비용

N, M = map(int, input().split())

v1, v2, e = map(int, input().split())

INF = float("inf")
graph = [[INF] * (N+1) for _ in range(N+1)]

for _ in range(M):
    u, v, d = map(int, input().split())
    graph[u][v] = d
    graph[v][u] = d

for i in range(1, N+1):
    graph[i][i] = 0


def floyd_warshall(graph):
    for k in range(1, N+1):
        for i in range(1, N+1):
            for j in range(1, N+1):
                graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])

floyd_warshall(graph)

# 따로 따로 가는 경우
res = graph[v1][e] + graph[v2][e]

for x in range(1, N+1):
    # 만나서 함께 가는 경우
    res = min(res, graph[v1][x] + graph[v2][x] + graph[x][e])

print(res if res != INF else -1)