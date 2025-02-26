n = int(input())
arr = list(map(int, input().split()))

# Please write your code here.
def sol(arr, n):
    for i in range(n):
        print(abs(arr[i]), end=' ')