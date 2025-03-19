# 1 ~ N의 서로 다른 점들과, 이 점들 중 임의의 두 점을 잇는 M개의 길이 있다.

# N개의 점 중 1 ~ P번까지의 점은 빨간점
# 모든 길은 한방향으로 이동 가능(Edge도 하나만 존재)

# M개의 길들을 이용해 점 A -> B까지 최소 비용으로 이동하고자 한다.

# 출발점과 도착점을 포함해 경로 내에 최소 하나 이상의 빨간점 포함되어있어야 이동

# 출발점, 도착점 쌍 Q개 중 빨간색 점을 최소 하나 이상 지나 갈 수 있는 경우가 몇개인지
# 가능한 경우 각 최소 비용의 총 합을 구하여라

N, M, P, Q = map(int, input().split())

INF = float('inf')
graph = [[INF]*(N+1) for _ in range(N+1)]

for _ in range(M):
    u, v, d = map(int, input().split())
    graph[u][v]= d 

for i in range(1, N+1):
    graph[i][i] = 0

def floyd_warshall(graph):    
    for k in range(1, N+1):
        for i in range(1, N+1):
            for j in range(1, N+1):
                graph[i][j] = min(graph[i][j], graph[i][k]+graph[k][j])

floyd_warshall(graph)

count = 0
res = 0
for _ in range(Q):
    A, B = map(int, input().split())
    distance = INF
    for p in range(1, P+1):
        distance = min(distance, graph[A][p] + graph[p][B])
    if distance >= INF:
        continue

    count += 1
    res += distance

print(count)
print(res)