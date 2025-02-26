n, m = map(int, input().split())
arr = list(map(int, input().split()))
queries = [tuple(map(int, input().split())) for _ in range(m)]

# Please write your code here.

def sol(N, M, queries):
    global arr

    for i in range(M):
        print(sum(arr[queries[i][0]-1:queries[i][1]-1]))