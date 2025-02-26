a, b = map(int, input().split())

# Please write your code here.
def sol(a, b):
    if a > b:
        return a+25, b*2
    else :
        return a*2, b+25
a, b = sol(a, b)
print(a, b)
