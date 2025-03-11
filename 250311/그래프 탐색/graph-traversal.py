from collections import defaultdict
N, M = map(int, input().split())

# N개의 정점과 M개의 간선으로 이루어진 양방향 그래프
# 1번 node에서 시작하여 주어진 Edge를 따라 이동했을 때
# 도달할 수 있는 서로 다른 Node의 개수(1번 제외)

graph = defaultdict(list)

for _ in range(M):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

visited = [1]
count = 0
def dfs(curr):    
    global count
    for next_node in graph[curr]:
        if next_node not in visited:
            visited.append(curr)
            count += 1
            dfs(next)

dfs(1)
print(count)