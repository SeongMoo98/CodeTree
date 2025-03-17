# 도착점 A에서 시작점 B가 나오기전까지 최단거리를 만족하는 경로 중
# 가장 수가 작은 곳으로 이동

# 만약 최단거리를 만족하는 경로가 여러개라면,
# 그 중 사전순으로 가장 앞선 경로를 찾기 위한 방법(번호가 작은순)

# 1. 모든 Edge를 뒤집고, 도착점을 시작점으로 하는 Dijkstra 알고리즘 진행
# 2. 시작점에서 출발하여 1 ~ N번까지 순회하며 최단 거리 경로 상에 존재할 수 있는 모든 Node를 찾아
#    이동하는 것을 도착점에 도달할때 까지 반복
from collections import defaultdict
import heapq
INF = float('inf')

# 양방향 그래프
# 정점 A에서 B까지의 최단 거리와 그 때의 경로를 구하여라
# 최단 경로가 여러개라면 사전순으로 앞선순(정점의 번호가 작은 순)
N, M = map(int, input().split())

graph = [[0] * (N+1) for _ in range(N+1)]
for _ in range(M):
    u, v, d = map(int, input().split())
    graph[u][v] = d
    graph[v][u] = d

# A -> B
A, B = map(int, input().split())

distances = [INF] *(N+1)
visited = [False] * (N + 1)

# 도착점을 시작으로 역 다익스트라
distances[B] = 0

# O(|V|^2) 다익스트라 코드
for i in range(1, N+1):
    min_index = -1
    # 아직 방문하지 않은 Node 중 distance 값이 가장 작은 Node 찾기
    for j in range(1, N+1):
        if visited[j]:
            continue
        if min_index == -1 or distances[min_index] > distances[j]:
            min_index = j

        # 최솟값에 해당하는 Node 방문 처리
        visited[min_index] = True

        # 최솟값에 해당하는 정점에 연결된 Edge를 보며
        # 시작점으로부터의 최단거리 값을 갱신
        for j in range(1, N+1):
            if graph[min_index][j] == 0:
                continue

            if distances[j] > distances[min_index] + graph[min_index][j]:
                distances[j] = distances[min_index] + graph[min_index][j]

# B에서 A로 가기위한 최단거리
print(distances[A])
# 도착점 A에서 시작점 B가 나오기전까지 최단거리를 만족하는 경로 중
# 가장 수가 작은 곳으로 이동
curr = A
print(A, end=' ')
while curr != B:
    for i in range(1, N+1):
        # i -> curr Edge가 없으면 Pass
        if graph[i][curr] == 0:
            continue

        # 만약 b -> ... -> i -> x ... -> a로 실제 최단거리가 나올 수 있는 상황이었다면,
        # i를 작은 번호부터 보고 있으므로 선택
        if distances[i] + graph[i][curr] == distances[curr]:
            curr = i
            break

    print(curr, end=' ')
    