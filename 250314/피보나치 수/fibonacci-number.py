N = int(input())

fibo = [0]*(45+1)
fibo[1], fibo[2] = 1

for i in range(3, len(fibo)):
    fibo[i] = fibo[i-1] +fibo[i-2]

print(fibo[N])