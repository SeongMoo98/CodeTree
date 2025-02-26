n, m = map(int, input().split())

def sol(n, m):
    max_num = 0
    for i in range(1, min(n, m)):
        if n % i == 0 and m % i == 0:
            max_num = i
    return max_num

print(sol(n,m))
# Please write your code here.