N = int(input())

num = 1
for i in range(N):
    for j in range(N):
        print(num, end=' ')
        if num < 9:
            num += 1
        else:
            num = 1
    print()