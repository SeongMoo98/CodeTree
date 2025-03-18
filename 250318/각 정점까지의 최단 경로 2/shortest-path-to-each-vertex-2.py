# 모든 정점 (i, j)에 대해
# 정점 i에서 출발하여 정점 j에 도착하기 위한 최단 거리
# Directed Graph
# ==> Floyd - Warshall

N, M = map(int, input().split())
INF = float('inf')
graph = [[INF] * (N+1) for _ in range(N+1)]

for _ in range(M):
    u, v, d = map(int, input().split())
    # 두 Vertex를 연결하는 Edge가 여러개 존재 가능
    graph[u][v] = min(graph[u][v], d)

# 자기 자신은 0
for i in range(1, N+1):
    graph[i][i] = 0

def floyd_warshall(graph):
    for k in range(1, N+1):
        for i in range(1, N+1):
            for j in range(1, N+1):
                if graph[i][j] > graph[i][k] + graph[k][j]:
                    graph[i][j] = graph[i][k] + graph[k][j]
                

floyd_warshall(graph)

for i in range(1, N+1):
    for j in range(1, N+1):
        if graph[i][j] == INF:
            print(-1, end=' ')
        else:
            print(graph[i][j], end=' ')
    print() 