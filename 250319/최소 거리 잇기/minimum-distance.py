import math

# 변수 선언 및 입력:
N, M = map(int, input().split())

parent = [0] * (N + 1)

# 그래프를 인접행렬로 표현
points = [(-1, -1)] * (N + 1)
for i in range(1, N + 1):
    points[i] = tuple(map(int, input().split()))

edges = []
for i in range(1, N + 1):
    for j in range(i + 1, N + 1):
        x1, y1 = points[i]
        x2, y2 = points[j]
        dist = math.sqrt((x1 - x2) * (x1 - x2) + (y1 - y2) * (y1 - y2))
        edges.append((dist, i, j))

# cost 순으로 오름차순 정렬을 진행합니다.
edges.sort()

# uf 값을 초기값을 적어줍니다.
for i in range(1, N + 1):
    parent[i] = i


def find(x):
    if parent[x] == x:
        return x
    parent[x] = find(parent[x])
    return parent[x]


def union(x, y):
    X = find(x)
    Y = find(y)
    parent[X] = Y


# m개의 간선 정보를 입력받습니다. 간선을 서로 연결해줍니다.
for _ in range(m):
    x, y = tuple(map(int, input().split()))
    
    union(x, y)

# dist가 낮은 간선부터 순서대로 보며
# 아직 두 노드가 연결이 되어있지 않을 경우에만
# 해당 간선을 선택하고 두 노드를 합쳐주면서
# mst를 만들어줍니다.
ans = 0
for dist, x, y in edges:
    # x, y가 연결되어 있지 않다면
    if find(x) != find(y):
        # 해당 간선은 MST에 속하는 간선이므로
        # 답을 갱신해주고
        # 두 노드를 연결해줍니다.

        ans += dist
        union(x, y)

# 모든 간선의 길이의 총합을 출력합니다.
print(f"{ans:.2f}")
