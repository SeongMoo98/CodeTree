# 1번부터 N번까지의 장소 사이를 이동

# 각 장소마다 직접적으로 연결된 도로 존재(단방향)

# i -> j까지 경유없이 이동하면 i행 j열에 해당하는 시간만큼,
# 경유하면 더 짧은 시간 가능
# ==> 플로이드 워셜

# M개의 질의에 대해 a -> b 까지의 최단 시간을 구하여라

N, M = map(int, input().split())

INF = float('inf')
graph = [[INF] *(N+1) for _ in range(N+1)]

for i in range(1, N+1):
    inputs = list(map(int, input().split()))
    for j in range(1, N+1):
        if inputs[j-1] == 0 and i != j:
            graph[i][j] = INF
        else:
            graph[i][j] = inputs[j-1]
    
def floyd_warshall(graph):
    for k in range(1, N+1):
        for i in range(1, N+1):
            for j in range(1, N+1):
                if graph[i][j] > graph[i][k] + graph[k][j]:
                    graph[i][j] = graph[i][k] + graph[k][j]

floyd_warshall(graph)

for _ in range(M):
    a, b = map(int, input().split())
    print(graph[a][b])


    
