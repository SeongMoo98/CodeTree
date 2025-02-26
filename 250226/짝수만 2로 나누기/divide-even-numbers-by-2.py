N = int(input())
arr = list(map(int, input()))

def sol(arr, N):
    for i in range(N):
        if arr[i] % 2 == 0:
            arr[i] /= 2

    return arr

arr = sol(arr, N)
print(' '.join(map(str, arr)))
