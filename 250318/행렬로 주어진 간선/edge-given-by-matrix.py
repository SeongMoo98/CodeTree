# N개의 정점이 존재하는 그래프에서 각 간선의 정보가 행렬로 주어진다
# 행렬의 [i][j]에 해당하는 정수가 1이면, Edge가 존재한다는 뜻
# 모든 정점에 대해, 서로의 정점으로 도달하는 경로가 있는지 없는지 구하여라

N = int(input())
INF = float('inf')

# graph[i][j]의 값이 존재하면 i -> j의 Edge가 존재
graph = [list(map(int, input().split())) for _ in range(N)]

for i in range(N):
    for j in range(N):
        if graph[i][j] == 0 and i != j:
            graph[i][j] = INF

def floyd_warshall(graph):
    for k in range(N):
        for i in range(N):
            for j in range(N):
                if graph[i][j] > graph[i][k] + graph[k][j]:
                    graph[i][j] = graph[i][k] + graph[k][j]

floyd_warshall(graph)
for i in range(N):
    for j in range(N):
        if i == j:
            print(1, end=' ')
        else:
            if graph[i][j] != INF:
                print(graph[i][j], end=' ')
    print()