a, b = map(int, input().split())

# Please write your code here.

def is_prime(num):
    if num == 1:
        return False
    elif num == 2:
        return True
    
    for i in range(2, num):
        if num % i == 0:
            return False
    return True

count = 0
for num in range(a, b+1):
    if is_prime(num):
        sum = num // 100 + num // 10 + num % 10
        if sum % 2 == 0:
            count += 1
print(count)
        
