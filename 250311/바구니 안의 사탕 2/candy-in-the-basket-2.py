N, K = map(int, input().split())

MAX_LEN = 100
positions = [0] * (MAX_LEN + 1)

for i in range(N):
    candy, pos = map(int, input().split())
    positions[pos] += candy

max_candy = 0
for i in range(MAX_LEN+1):
    start, end = i-K, i + K + 1
    if i - K < 0 :
        start = 0
    if i + K > MAX_LEN + 2:
        end = MAX_LEN + 1

    temp = positions[start:end]
    max_candy = max(max_candy, sum(temp))
print(max_candy)


