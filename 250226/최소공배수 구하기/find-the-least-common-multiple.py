n, m = map(int, input())

def sol(n, m):
    min_num = n*m+10

    for i in range(min(n, m), n*m+1):
        if i % n == 0 and i % m == 0:
            min_num = min(i, min_num)
    return min_num

print(sol(n,m))
