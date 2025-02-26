a, b = map(int, input().split())

# Please write your code here.

count = 0
for num in range(a, b+1):
    if num % 2 != 0 or num % 5 != 5:
        if num % 3 == 0 and num % 9 !=0:
            continue
        else:
            count += 1
print(count)