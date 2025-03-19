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
        parent[a] = b

for _ in range(M):
    a, b = map(int, input().split())
    
    union(a, b)

# 4 2 1 .. k개
# k개의 순서로 이동 가능한지
path = [0] + list(map(int, input().split()))

# 경로를 이동하는 것이 가능하면 True, 아니라면 False를 기록합니다.
is_pos = True
   
# 만약 경로의 i번째 노드에서 i + 1번째 노드가 연결되어 있지 않으면 이동하는 것이 불가능합니다.
# 이는 대표 번호가 동일한지로 판단 가능합니다.
for i in range(1, K):
    if find(path[i]) != find(path[i + 1]):
        is_pos = False

if is_pos: 
    print(1)
else:
    print(0)