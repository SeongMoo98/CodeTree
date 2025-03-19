import sys
input = sys.stdin.readline
# 1 ~ N까지의 정점

# x a b : 정점 a와 b를 간선으로 연결
# y a : 정점 a와 연결되어 있는 정점의 개수 출력

N, M = map(int, input().split())

parent = [i for i in range(N+1)]
# 각 Node에 연결된 Node 수
res = [1] * (N+1)

def find(x):
    if parent[x] == x:
        return x

    parent[x] = find(parent[x])
    return parent[x]

def union(a, b):
    a, b = find(a), find(b)

    if a != b:
        parent[a] = b
        res[b] += res[a]


for _ in range(M):
    inputs = input().split()
    if inputs[0] == 'x':
        a, b = int(inputs[1]), int(inputs[2])
        union(a, b)
    else:
        a = int(inputs[1])
        print(res[a])

