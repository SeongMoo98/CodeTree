N = int(input())

res = 0
# Please write your code here.
def sol(depth):
    if depth == N+1:
        return 
    sol(depth+1, res+depth)



print(sol(1), res)