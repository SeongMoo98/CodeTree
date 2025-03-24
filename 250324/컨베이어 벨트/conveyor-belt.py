# 시계방향으로 한칸씩 회전하는 컨베이어 벨트

# N개씩 2N개의 숫자
# 1초에 한칸씩 움직임

# T초의 시간이 흐른 뒤 컨베이어 벨트에 적힌 숫자들의 상태?

N, T = map(int, input().split())

arr = []
for i in range(2):
    arr.extend(list(map(int, input().split())))

for t in range(T):
    temp = arr[-1]
    arr[1:] = arr[0:2*N-1]
    arr[0] = temp


for i in range(2*N):
    if i == N:
        print()
    print(arr[i], end=' ')