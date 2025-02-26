N = int(input())

res = 0
# Please write your code here.
def sol(depth):
    global res
    if depth == N+1:
        return 
    res += depth
    sol(depth+1)



sol(1)
print(res)