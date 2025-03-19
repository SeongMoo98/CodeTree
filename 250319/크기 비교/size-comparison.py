# 서로 크기가 다른 정수 N개에 대해
# 1 ~ N번까지의 정수중 중 임의의 두 정수와 크기를 비교한 결과가 M번 주어진다

# M번의 비교결과를 통해, 각 정수가 다른 몇 개의 정수와 크기 비교 결과를 알수없는지 구하여라

N, M = map(int, input().split())

INF = float('inf')
graph = [[INF]*(N+1) for _ in range(N+1)]
# 두 개의 정수가 공백을 두고 주어지는데. 앞의 정수가 뒤의 정수보다 숫자가 크다는 뜻

for _ in range(M):
    a, b = map(int, input().split())
    # a > b라는 뜻
    # 이를 1이라고 하자
    graph[a][b] = 1
for i in range(1, N+1):
    graph[i][i] = 0

def floyd_warshall(graph):
    for k in range(1, N+1):
        for i in range(1, N+1):
            for j in range(1, N+1):
                graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])

print(grpah)