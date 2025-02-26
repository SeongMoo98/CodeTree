y = int(input())

def sol(y):
    if y % 4 == 0:
        if y % 100 == 0 and y % 400 != 0:
            return False
        else:
            return True
    return False

if sol(y):
    print("true")
else:
    print("false")
