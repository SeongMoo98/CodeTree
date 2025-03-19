# N개의 정점, M개의 Edge

# 간선을 적절하게 뺴서 모든 정점은 연결되면서, 가중치를 최대한 많이 지우고 싶다

# ==> 남아있는 간선의 합이 최소
# ==> 크루스칼

N, M = map(int, input().split())

edges = []
res = 0
for _ in range(M):
    u, v, d = map(int, input().split())
    edges.append((d, u, v))
    res += d
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
        if find(u) != find(v):
            union(u, v)
            MST.append(edge)
            total_weight += w

    return MST, total_weight

MST, total_weight = kruskal(edges)

res -= total_weight

print(res)
