# 각 간선은 0, 1 두가지 종류가 있다.

# 0 : 위협이 있어 아이언맨을 고용해야지 지나갈 수 있다.
# 1 : 위햡 x

# 0에 해당하는 간선을 k번 지나가면 비용은 k^2의 비용

# 각 간선은 이미 지나간 간선을 다시 지나갈 때 비용 계산 x

# N개의 Vertex를 모두 한번씩 지나간다고 할때
# 이때, 최대가 되는 경로와, 최소가 되는 경로의 비용의 차를 구하여라

# 그냥 edge와, 최소 -edge

N, M = map(int, input().split())

parent = [i for i in range(N+1)]
edges = []
negative_edges = []

for _ in range(M):
    u, v, t = map(int, input().split())
    # 0 간선이 위협이니까 1의 비용을 가진다고 하자
    t = 0 if t == 1 else 1
    edges.append((t, u, v))
    negative_edges.append((-t, u, v))

edges.sort()
negative_edges.sort()

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
parent = [i for i in range(N+1)]
neg_MST, neg_total_weight = kruskal(negative_edges)


print((neg_total_weight)**2 - total_weight**2)
