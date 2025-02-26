a, o, c = map(str, input().split())
a, c = int(a), int(c)

def sol(a,o,c):
    if o == "+":
        return f"{a} {o} {c} = {a+c}"
    elif o =="-":
        return f"{a} {o} {c} = {a-c}"
    elif o == '*':
        return f"{a} {o} {c} = {a*c}"
    elif o == '/':
        return f"{a} {o} {c} = {a//c}"
    else:
        return False

print(sol(a, o ,c))