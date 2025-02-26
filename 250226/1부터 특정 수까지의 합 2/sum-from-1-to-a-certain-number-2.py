N = int(input())

res = 0
# Please write your code here.
def sol(n):
    if n == 0:
        return 0 
    
    return sol(n-1) + n



print(sol(N))
