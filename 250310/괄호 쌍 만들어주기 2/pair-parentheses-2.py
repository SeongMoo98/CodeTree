A = list(input())

# Please write your code here.
count = 0

for i in range(len(A)-1):
    if A[i] == "(" and A[i+1] == "(":
        for j in range(i+2, len(A)-1):
            if A[j] == ")" and A[j+1] == ")":
                count += 1

print(count)