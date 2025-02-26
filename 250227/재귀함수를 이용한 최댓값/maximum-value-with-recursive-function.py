N = int(input())
arr = list(map(int, input().split()))


def sol(arr, N):
    if len(arr) == 1 or len(arr) == 2:
        return max(arr)
    N = N // 2
    return max(sol(arr[:N], N), sol(arr[N:], N))

print(sol(arr, N))