M, D = map(int, input().split())

# Please write your code here.

# 2021년 M월 D일이 존재하는지?(2월 28일까지 있다)

three_one = [1, 3, 5, 7, 8, 10 ,12]
three_zero = [4, 6, 9, 11]

flag = False
if M == 2:
    if D <= 28:
        flag = True
elif M in three_one:
    if D <= 31:
        flag = True
elif M in three_zero:
    if D <= 30:
        flag = True
if flag:
    print("Yes")
else:
    print("No")