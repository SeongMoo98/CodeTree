n, m = map(int, input().split())
A = list(map(int, input().split()))

# Please write your code here.

def sol(N, M, A):
    res = 0
    for i in range(N):
        if M == 0:
            break
        res += A[M-1]
        if M % 2 == 0:
            M = int(M/2)
        else:
            M -= 1

    return res
print(sol(n, m, A))