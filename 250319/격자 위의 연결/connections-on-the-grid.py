# N x M 격자, 각 칸을 연결하는 선 존재

# 모든 칸이 연결되도록 선을 연결하되 연결된 모든선의 가중치의 합이 최소가 되게하라

N, M = map(int, input().split())

parent = [i for i in range(N*M+1)]

def find(x):
    if parent[x] == x:
        return x

    parent[x] = find(parent[x])
    return parent[x]

def union(a, b):
    a, b = find(a), find(b)

    if a != b:
        parent[a] = b

edges = []

# 가로 M-1개
for i in range(N):
    weights = list(map(int, input().split()))
    for j in range(M-1):
        edges.append((weights[j], M * i + j + 1, M * i + j + 2))

# - 모양 Edge
# [0][0] - [0][1], [0][1]- [0][2]
# [1][0] - [1][1], [1][1] - [1][2]

for i in range(N-1):
    weights = list(map(int, input().split()))
    for j in range(M):
        edges.append((weights[j], M * i + j + 1, M * (i+1) + j + 1))

edges.sort()

print(edges)

def kruskal(edges):
    MST = []
    total_weight = 0

    for edge in edges:
        w, u, v = edge
        if find(u) != find(v):
            union(u, v)
            MST.append(edge)
            total_weight += w

    return total_weight


print(kruskal(edges))
    
