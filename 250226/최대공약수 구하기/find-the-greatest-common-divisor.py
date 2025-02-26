n, m = map(int, input().split())

max_num = 0
for i in range(1, min(n, m)):
    if n % i == 0 and m % i == 0:
        max_num = i
print(max_num)
# Please write your code here.