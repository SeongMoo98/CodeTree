# N개의 정점과 M개의 간선
# 임의의 서로 다른 두 정점 사이를 왕복하는데 이용하는 
# Edge들의 가중치 총합이 가장 낮은경우를 구하여라

# Directed Graph

N, M = map(int, input().split())

INF = float('inf')

graph = [[INF] * (N+1) for _ in range(N+1)]

for i in range(M):
    u, v, d = map(int, input().split())
    graph[u][v] = d

for i in range(1, N+1):
    graph[i][i] = 0


def floyd_warshall(graph):
    for k in range(1, N+1):
        for i in range(1, N+1):
            for j in range(1, N+1):
                if graph[i][j] > graph[i][k] + graph[k][j]:
                    graph[i][j] = graph[i][k] + graph[k][j]

floyd_warshall(graph)

res = INF
for i in range(1, N+1):
    for j in range(1, N+1):
        res = min(res, graph[i][j] + graph[j][i])
print(res)