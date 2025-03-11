n, k = map(int, input().split())
arr = list(map(int, input().split()))

# Please write your code here.
max_sum = 0
if n == k:
    print(sum(arr))
for i in range(n-k):
    max_sum = max(max_sum, sum(arr[i:i+k]))
print(max_sum)
