# 1 ~ N번까지 N개의 정점과 M개의 간선
# MST를 구하여라

N, M = map(int, input().split())

parent = [i for i in range(N+1)]
def find(x):
    if parent[x] == x:
        return x

    return find(parent[x])

def union(a, b):
    a, b = find(a), find(b)

    if a != b:
        parent[a] = b


edges = []

for _ in range(M):
    u, v, weight = map(int, input().split())
    edges.append((weight, u, v))

edges.sort()

def kruskal(edges):
    MST = []
    total_weight = 0
    for edge in edges:
        weight, u, v = edge
        if find(u) != find(v):
            union(u, v)
            MST.append(edge)
            total_weight += weight

    return total_weight

print(kruskal(edges))