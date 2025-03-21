# MST를 구하여라

N, M = map(int, input().split())
edges = []
for _ in range(M):
    u, v, d = map(int, input().split())
    edges.append((d, u, v))

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

edges.sort()
def kruskal(edges):
    MST, total_weight = [], 0
    for edge in edges:
        w, u, v = edge
        if find(u) != find(v):
            union(u, v)
            MST.append(edge)
            total_weight += w

    return MST, total_weight

MST, total_weight = kruskal(edges)

print(total_weight)