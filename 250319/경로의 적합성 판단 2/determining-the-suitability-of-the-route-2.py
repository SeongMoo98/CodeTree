# N개의 정점, M개의 Edge, Undirected Graph

# k개의 점으로 이루어진 순서가 주어졌을 때, 그래프의 주어진 순서대로 이동이 가능한지 확인
N, M, K = map(int, input().split())

parent = [i for i in range(N+1)]

def find(x):
    if parent[x] == x:
        return x

    return find(parent[x])

def union(a, b):
    a, b = find(a), find(b)

    if a != b:
        parent[b] = a

for _ in range(M):
    a, b = map(int, input().split())
    # a가 부모가 됨
    union(a, b)


# 4 2 1 .. k개
# k개의 순서로 이동 가능한지
nodes = list(map(int, input().split()))

res = 1
for i in range(K-1):
    if parent[nodes[i]] != parent[nodes[i+1]]:
        res = 0
        break
    
print(res)