# 1 ~ N, M개의 Edge

# N개의 Vertex는 a, b로 구분된다

# 그래프에서 서로 다른 종류의 정점을 잇는 Edge만을 이용해 Spanning Tree를 만들때,
# 간선 가중치의 합이 최소가 되는 MST를 구하여라

N, M = map(int, input().split())

vertexs = [0] + list(map(str, input().split()))

edges = []
for _ in range(M):
    u, v, w = map(int, input().split())
    edges.append((w, u, v))

edges.sort()

parent = [i for i in range(N+1)]

def find(x):
    if parent[x] == x:
        return x
    parent[x] = find(parent[x])
    return parent[x]

def union(a, b):
    a, b = find(a), find(b)

    if a != b:
        parent[a] = b

def kruskal(edges):
    MST = []
    total_weight = 0

    for edge in edges:
        w, u, v = edge
        if find(u) != find(v) and vertexs[u] != vertexs[v]:
            union(u, v)
            MST.append(edge)
            total_weight += w

    return MST, total_weight


MST, total_weight = kruskal(edges)

if len(MST) != N-1:
    print(-1)
else:
    print(total_weight)
