n = int(input())
A = list(map(int, input().split()))

# Please write your code here.


count = 0
for i in range(n-2):
    for j in range(i+1, n-1):
        for k in range(j+1, n):
            if A[i] <= A[j] and A[j] <= A[k]:
                count += 1

print(count)
