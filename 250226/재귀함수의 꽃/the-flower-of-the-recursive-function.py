N = int(input())

# Please write your code here.
res = []
def sol(depth):
    if depth == 0:
        return

    res.append(depth)
    sol(depth-1)
    res.append(depth)
    

sol(N)

print(' '.join(map(str, res)))