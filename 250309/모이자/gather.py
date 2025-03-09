n = int(input())
A = list(map(int, input().split()))

# Please write your code here.

min_val = float('inf')

for std in range(n):
    dist = 0
    for i in range(n):
        dist += abs(std - i) * A[i]
    min_val = min(min_val, dist)

print(min_val)