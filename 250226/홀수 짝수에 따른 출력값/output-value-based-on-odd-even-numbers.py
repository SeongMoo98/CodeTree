N = int(input())

# Please write your code here.
def sol(num):
    if num == 1 or num == 2:
        return num

    return num + sol(num-2)

if N % 2 == 0:
    print(sol(N))
else:
    print(sol(N))