# 수직선상의 N개의 선분이 주어졌을 때, 
# 서로 겹치지 않고 고를 수 있는 가장 많은 선분의 수
# 끝점을 겅유하는 것 역시 겹친 것

N = int(input())
lines = [[0, 0]] + [list(map(int, input().split())) for _ in range(N)]

res = 0

def backtrack(curr, ans, visited):
    global res

    l, r = lines[curr]
    if visited[l] == True or visited[r] == True:
        return 
    else:
        for idx in range(l, r+1):
            visited[idx] = True


    if curr == N:
        res = max(res, len(ans))
        return 

    for i in range(curr+1, N+1):
        ans.append(lines[i])
        backtrack(i, ans, visited)
        ans.pop() 

# 이건 Line 0을 꼭 포함하는 코드다
# backtrack(0, [], [False] * 1001)

backtrack(0, [], [False] * 1001)
print(res)