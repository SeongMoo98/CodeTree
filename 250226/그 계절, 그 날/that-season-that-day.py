Y, M, D = map(int, input().split())

def is_yoon(Y):
    flag = False
    if Y % 4 == 0:
        flag = True
        if Y % 100 == 0 and Y % 400 != 0:
            flag = False

    return flag

def has_month_day(Y, M, D):
    three_one = [1, 3, 5, 7, 8, 10 ,12]
    three_zero = [4, 6, 9, 11]

    flag = False
    if M == 2:
        if is_yoon(Y):
            if D <= 29:
                flag = True
        else:
            if D <= 28:
                flag = True
    elif M in three_one:
        if D <= 31:
            flag = True
    elif M in three_zero:
        if D <= 30:
            flag = True

    if flag:
        if M in [3, 4, 5]:
            print("Spring")
        elif M in [6, 7, 8]:
            print("Summer")
        elif M in [9, 10, 11]:
            print("Fall")
        elif M in [12, 1, 2]:
            print("Winter")
    else:
        print(-1)

has_month_day(Y, M, D)