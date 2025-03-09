a = input()

# Please write your code here.

a = list(a)

for i in range(len(a)):
    if a[i] == '0':
        a[i] = '1'
        break

num = 0
for i in range(len(a)):
    if a[i] == '1':
        num += 2 ** (len(a) - i - 1)
print(num)