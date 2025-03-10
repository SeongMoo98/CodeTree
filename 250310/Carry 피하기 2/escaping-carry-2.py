n = int(input())
arr = [int(input()) for _ in range(n)]

# Please write your code here.

# N개의 수 
# 그 중 서로 다른 3개의 수를 골랐을 때 "carry"가 발생하지 않으면서
# 나올 수 있는 수의 합의 최댓값을 계산
# 모든 수 쌍에서 carry가 발생할 경우, -1

# "carry"
# 수와 수를 더했을때, 10의 자리를 넘기는 것

max_val = -1
carry = False
for i in range(n-2):
    for j in range(i+1, n-1):
        for k in range(j+1, n):
            carry = False
            num1, num2, num3 = arr[i], arr[j], arr[k]

            while num1 !=0 or num2 !=0 or num3 !=0:
                carry_sum = num1 % 10 + num2 % 10 + num3 % 10
                # carry가 발생 -> 이 조합은 안된다
                if carry_sum >= 10:
                    carry = True
                    break
                num1 //= 10
                num2 //= 10
                num3 //= 10
            if carry == False:
                max_val = max(max_val, arr[i]+arr[j]+arr[k])

print(max_val)
        