n1, n2 = map(int, input().split())
# n1 : 수열 a의 길이
a = list(map(int, input().split()))
# n2 : 수열 b의 길이
b = list(map(int, input().split()))

# Please write your code here.
# 수열 b가 수열 a의 연속부분수열인지 판다
# 수열 b가 수열 a의 원소들을 연속으로 뽑았을 때 나올 수 있는 수열

# a에서 뽑아야하는 연속 수열 n2개

res = False
for i in range(n1):
    if i + n2 > n1:
        break
    
    if b == a[i:i+n2]:
        res = True
        break

if res:
    print("Yes")
else:
    print("No")