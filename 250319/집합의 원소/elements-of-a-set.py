# 집합 관리 프로그램
# 초기 : 자기 자신만이 포함된 집합

# 0 a b : a가 포함된 집합과 b과 포함된 집합을 합친다.
# 1 a b : a와 b가 같은 집합에 있다면 1, 그렇지 않다면 0

N, M = map(int, input().split())

parent = [i for i in range(N+1)]

def find(x):
    if parent[x] == x:
        return x

    return find(parent[x])

def union(a, b):
    parent_a, parent_b = find(a), find(b)

    if parent_a != parent_b:
        parent[parent_a] = parent_b

for _ in range(M):
    num, a, b = map(int, input().split())
    # Union
    if num == 0:
        union(a, b)
    # Find
    elif num == 1:
        a, b = find(a), find(b)
        if a == b:
            print(1)
        else:
            print(0)

            