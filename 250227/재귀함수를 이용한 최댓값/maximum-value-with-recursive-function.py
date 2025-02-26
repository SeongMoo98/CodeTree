N = int(input())
arr = list(map(int, input().split()))


# def sol(arr, N):
#     if len(arr) == 0:
#         return 0
    
#     if len(arr) == 1:
#         return arr[0]
#     N = N // 2
#     return max(sol(arr[:N], len(arr[:N])), sol(arr[N:], len(arr[N:])))

# print(sol(arr, N))


def max_value(idx):
    if idx == 0:
        return arr[0]
    return max(max_value(idx-1), arr[idx])

print(max_value(N-1))