# 3차원 좌표평면 위체 N개의 점
# 모든 점을 연결

# 두개의 점을 연결하는데 드는 비용 : min(x의 차, y의 차, z의 차)

N = int(input())

# 3차원 좌표평면 위의 N개의 점
points = [(-1, -1, -1)] + [tuple(map(int, input().split())) for _ in range(N)]

parent = [i for i in range(N+1)]

edges = []
for i in range(1, N+1):
    # (x, y, z)
    p1 = points[i]
    for j in range(i+1, N+1):
        p2 = points[j]
        cost = min(abs(p1[0]-p2[0]), abs(p1[1]-p2[1]), abs(p1[2]-p2[2]) )
        edges.append((cost, i, j))
    
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

edges.sort()
MST, total_weight = kruskal(edges)
print(total_weight)