import sys

INT_MAX = sys.maxsize

# 변수 선언 및 입력:
n, m = tuple(map(int, input().split()))
graph = [
    [0] * (n + 1)
    for _ in range(n + 1)
]
visited = [False] * (n + 1)

# 그래프에 있는 모든 노드들에 대해
# 초기값을 전부 아주 큰 값으로 설정
dist = [INT_MAX] * (n + 1)

# 그래프를 인접행렬로 표현
# 양방향 그래프이므로 양쪽 다 표시해줍니다.
for _ in range(m):
    x, y, z = tuple(map(int, input().split()))
    graph[x][y] = z
    graph[y][x] = z

# 시작, 끝 위치를 입력으로 받습니다.
a, b = tuple(map(int, input().split()))

# 시작위치에는 dist값을 0으로 설정
dist[b] = 0

# O(|V|^2) 다익스트라 코드
for i in range(1, n + 1):
    # V개의 정점 중 
    # 아직 방문하지 않은 정점 중
    # dist값이 가장 작은 정점을 찾아줍니다.
    min_index = -1
    for j in range(1, n + 1):
        if visited[j]:
            continue
        
        if min_index == -1 or dist[min_index] > dist[j]:
            min_index = j

    # 최솟값에 해당하는 정점에 방문 표시를 진행합니다.
    visited[min_index] = True

    # 최솟값에 해당하는 정점에 연결된 간선들을 보며
    # 시작점으로부터의 최단거리 값을 갱신해줍니다.
    for j in range(1, n + 1):
        # 간선이 존재하지 않는 경우에는 넘어갑니다.
        if graph[min_index][j] == 0:
            continue

        if dist[j] > dist[min_index] + graph[min_index][j]:
            dist[j] = dist[min_index] + graph[min_index][j]

# 정점 B에서 정점 A로 가기 위한 최단거리를 출력합니다.
print(dist[a])

# 도착지 A에서 시작하여
# 시작점 B가 나오기 전까지
# 최단거리를 만족하는 경로 중
# 가장 간선 번호가 작은 곳으로 이동합니다.
x = a
print(x, end=" ")
while x != b:
    for i in range(1, n + 1):
        # 간선이 존재하지 않는 경우에는 넘어갑니다.
        if graph[i][x] == 0:
            continue

        # 만약 b -> ... -> i -> x ... -> a로 
        # 실제 최단거리가 나올 수 있는 상황이었다면
        # i를 작은 번호부터 보고 있으므로
        # 바로 선택해줍니다.
        if dist[i] + graph[i][x] == dist[x]:
            x = i
            break

    print(x, end=" ")
