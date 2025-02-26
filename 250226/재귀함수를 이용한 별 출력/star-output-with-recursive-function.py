n = int(input())

# Please write your code here.
def sol(depth):
    if depth == n+1:
        return

    for _ in range(depth):
        print('*', end='')
    print()
    sol(depth+1)
sol(1)