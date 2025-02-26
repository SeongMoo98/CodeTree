N = int(input())

# Please write your code here.
def sol(N, count):

    if N == 1:
        return count

    if N % 2 == 0:
        N = N // 2
    else:
        N = N // 3
    return sol(N, count + 1)

print(sol(N, 0))