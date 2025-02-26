a, b = map(int, input().split())

# Please write your code here.
def sol(a, b):
    mini = min(a, b)
    maxi = max(a, b)

    return maxi+25, mini*2

maxi, mini = sol(a, b)
print(mini, maxi)
