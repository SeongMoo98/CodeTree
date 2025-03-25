# 시계 방향으로 한칸씩 회전하면서 회전하는 삼각형 모양의 컨베이어 벨트

# T초의 시간이 흐른뒤 벨트에 놓여있는 숫자의 상태 출력
# 입력 : 
# 1 2 4
# 5 9 3
# 6 5 1

N, T = map(int, input().split())
arr = []
for i in range(N):
    arr.extend(list(map(int, input().split())))
    
for t in range(T):
    temp = arr[-1]
    arr[1:] = arr[0:len(arr)-1]
    arr[0] = temp

for i in range(N):
    for j in range(N):
        print(arr[i*3 + j], end=' ')
    print()