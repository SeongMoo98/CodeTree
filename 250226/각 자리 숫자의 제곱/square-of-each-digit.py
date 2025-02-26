N = int(input())

# Please write your code here.

def power(N):

    if N == 0:
        return 0

    return power(N // 10) + (N % 10)**2

print(power(N))