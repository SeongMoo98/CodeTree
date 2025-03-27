# 2048 게임
# 상하좌우 한 방향을 정하면, 모든 숫자들이 해당 방향으로 이동

# 같은 숫자끼리 만나게 되면 두 숫자가 합쳐짐(연쇄적으로 합쳐지진 않는다)

# 특정 방향으로 움직인 이후 결과

arr = [list(map(int, input().split())) for _ in range(4)]
direction = input()

# L, R, U, D 으로 움직임

# 시계방향 회전
def rotate():
    global arr
    arr = list(map(list, zip(*arr[::-1])))

def move_left():

    new_arr = [[0] * 4 for _ in range(4)]
    # 왼쪽으로 밀기
    for i in range(4):
        temp = []
        for j in range(4):
            if arr[i][j] != 0:
                temp.append(arr[i][j])
        temp_idx = 0
        arr_idx = 0
        while temp_idx < len(temp):
            if temp_idx == len(temp)-1:
                new_arr[i][arr_idx] = temp[temp_idx]
                break
                
            if temp[temp_idx] == temp[temp_idx+1]:
                new_arr[i][arr_idx] = 2 * temp[temp_idx]
                temp_idx += 2
            else:
                new_arr[i][arr_idx] = temp[temp_idx]
                temp_idx += 1
            arr_idx+= 1
    for i in range(4):
        for j in range(4):
            arr[i][j] = new_arr[i][j]


# 회전해서 정한 한 방향으로만 이동
if direction == "L":
    move_left()
elif direction == "R":
    for _ in range(2):
        rotate()
    move_left()
    for _ in range(2):
        rotate()
elif direction == "U":
    for _ in range(3):
        rotate()
    move_left()
    rotate()
elif direction == "D":
    rotate()
    move_left()
    for _ in range(3):
        rotate()

for i in range(4):
    for j in range(4):
        print(arr[i][j], end=' ')
    print()