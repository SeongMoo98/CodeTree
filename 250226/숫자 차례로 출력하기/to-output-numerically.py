N = int(input())

# 1 ~ N
def sol1(depth):

    if depth == N + 1:
        return

    print(depth, end=' ')
    sol1(depth+1)


# N ~ 1
def sol2(depth):
    if depth == N+1:
        return
    sol2(depth+1)
    print(depth, end=' ')

sol1(1)
print()
sol2(1)