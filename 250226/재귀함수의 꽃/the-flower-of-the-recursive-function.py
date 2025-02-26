N = int(input())

# Please write your code here.
def sol(depth):
    if depth == 0:
        return

    print(depth, end=' ')
    sol(depth-1)
    print(depth, end=' ')
    

sol(N)
