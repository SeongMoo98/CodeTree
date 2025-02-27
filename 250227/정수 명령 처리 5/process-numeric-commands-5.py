N = int(input())

arr = []
for i in range(N):
    input_string = input().split()

    if len(input_string) == 1:
        op = input_string[0]
    else:
        op, num = input_string
        num = int(num)

    if op == "push_back":
        arr.append(num)

    if op == 'get':
        print(arr[num-1])

    if op == 'pop_back':
        arr.pop()

    if op == 'size':
        print(len(arr))