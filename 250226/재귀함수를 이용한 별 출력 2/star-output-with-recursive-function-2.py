n = int(input())

def sol(depth):
    if depth == 0:
        return

    for _ in range(depth):
        print("*", end =' ')
    print()
    sol(depth-1)
    for _ in range(depth):
        print("*", end=' ')
    print()

sol(n)