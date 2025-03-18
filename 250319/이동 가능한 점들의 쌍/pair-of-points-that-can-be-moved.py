# 1 ~ N의 서로 다른 점들과, 이 점들 중 임의의 두 점을 잇는 M개의 길이 있다.

# N개의 점 중 1 ~ P번까지의 점은 빨간점
# 모든 길은 한방향으로 이동 가능(Edge도 하나만 존재)

# M개의 길들을 이용해 점 A -> B까지 최소 비용으로 이동하고자 한다.

# 출발점과 도착점을 포함해 경로 내에 최소 하나 이상의 빨간점 포함

# 또, 한개의 점을 여러번 방문해도 괜찮다

# 주어진 출발점, 도착점들 쌍 Q개 중 빨간색 점을 최소 하나 이상 지나갈 수 있는 경우가
# 몇개인지 구하고, 가능한 경우 각 최소비용의 총합을 구하여라

N, M, P, Q = map(int, input().split())

INF = float('inf')
graph = [[INF]*(N+1) for _ in range(N+1)]
# 빨간점을 방문했는지 확인
visited = [[False] *(N+1) for _ in range(N+1)]

for _ in range(M):
    u, v, d = map(int, input().split())
    if 1 <= u <= P or 1 <= v <= P:
        visited[u][v] = True
    graph[u][v]= d 

for i in range(1, N+1):
    if 1 <= i <= P:
        visited[i][i] = True
    graph[i][i] = 0

def floyd_warshall(graph):    
    for k in range(1, N+1):
        for i in range(1, N+1):
            for j in range(1, N+1):
                if graph[i][j] > graph[i][k] + graph[k][j]:
                    if 1 <= i <= P or 1 <= j <= P or  1 <= k <= P \
                    or visited[i][k] or visited[k][j]:
                        visited[i][j] = True
                    graph[i][j] = graph[i][k] + graph[k][j]

floyd_warshall(graph)

count = 0
res = 0
for _ in range(Q):
    A, B = map(int, input().split())
    if graph[A][B] != INF and visited[A][B]:
        count += 1
        res += graph[A][B]

print(count)
print(res)