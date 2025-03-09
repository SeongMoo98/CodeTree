A = input()

# Please write your code here.

# 여는 괄호와 닫는 괄호로 쌍을 이룰 수 있는 서로 다른 가짓수를 구하여랴

count = 0
for i in range(len(A)):
    for j in range(i+1, len(A)):
        if A[i] == "(" and A[j] == ")":
            count += 1

print(count)
            