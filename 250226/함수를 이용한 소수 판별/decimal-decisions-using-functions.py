a, b = map(int, input().split())

# Please write your code here.
def is_prime(num):
    if num == 1 or num == 2:
        return True
    for i in range(2, num):
        if num % i == 0:
            return False

    return True
def sol(A, B):
    res = 0

    for num in range(A, B+1):
        if is_prime(num):
            res += num

    return res
print(sol(a, b))