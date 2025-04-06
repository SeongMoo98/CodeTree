# 메이즈 러너

# M명의 참가자가 미로탈출 게임

# 미로(좌상단이 (1, 1))
# N x N 격자
# 빈칸 : 이동이 가능한 칸
# 벽 : 이동할 수 없는 칸, 1 ~ 9의 내구도를 가짐(회전할 때 내구도 -1), 내구도가 0이 되면 빈 칸으로 변경
# 출구 : 참가자가 출구에 도착하면 탈출


# K초 동안 위의 과정을 반복
# 만약 K초 전에 모든 참가자가 탈출에 성공하면 게임 종료
# 게임이 종료됐을 때, 모든 참가자들의 이동거리의 합과 출구좌표 출력

# 격자 크기, 사람 수, 턴 수
# N <= 10, M <= 10, K <= 100
N, M, K = map(int, input().split())

# 미로 정보(0 : 빈칸, 1 ~ 9 : 벽의 내구도)
# -1 : 출구, -2 ~ : 사람
matrix = [list(map(int, input().split())) for _ in range(N)]

# 참가자의 좌표, 탈출 여부
people = dict()
exited = dict()
dist = dict()
for i in range(1, M+1):
    x, y = map(lambda x: int(x)-1, input().split())
    # -2, -3, ...이 people, exit의 key
    people[i] = (x, y)
    exited[i] = False
    dist[i] = 0
    
# 출구의 좌표
# 출구는 빈 칸에만 주어지며, 참가자의 좌표와 겹치지 않는다
ei, ej = map(lambda x:int(x)-1, input().split())

# 이게 아니라 2시간 동안 이제
# 사람, 출구 회전에 대해 구현
# 왜냐하면 보드 위에 여러명 존재 가능

def move_people():
    # 1초마다 모든 참가자가 한 칸씩 움직인다.
    # 2. 모든 참가자는 동시에 움직인다(상하좌우)
    # 3. 움직인 칸은 현재 머물러 있던 칸보다 출구까지의 최단거리(맨해튼 거리)가 가까워야한다.
    # 4. 움직일 수 있는 칸이 2개 이상이면 상,하로 움직이는 것을 우선시
    # 5. 참가자가 움직일 수 없는 상황이라면, 움직이지 않는다
    # 6. 한 칸에 2명이상의 참가자가 있을 수 있다.
    global people, exited, dist, matrix, ei, ej

    for num, (ci, cj) in people.items():
        # 이미 탈출한 사람
        if exited[num] == True:
            continue
        curr_dist = abs(ci - ei) + abs(cj - ej)
        # 상, 하, 좌, 우(왜냐하면 상 하 우선)
        for di, dj in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            ni, nj = ci + di, cj + dj
            # 범위 내, 벽 x or 출구
            if 0 <= ni < N and 0 <= nj < N and (matrix[ni][nj] == 0 or (ni, nj) == (ei, ej)):
                next_dist = abs(ni - ei) + abs(nj - ej)
                # 이동거리가 줄었을 때 이동
                if next_dist < curr_dist:
                    # 출구라면 탈출 처리
                    if (ni, nj) == (ei, ej):
                        exited[num] = True
                    people[num] = (ni, nj)
                    dist[num] += 1
                    break
                
def find_square():
    # 1. 한 명 이상의 참가자와 출구를 포함한 가장 작은 정사각형을 잡는다
    # 2. 가장 작은 크기를 갖는 정사각형이 2개 이상이라면 좌상단 좌표의 i, 그래도 같으면 j가 작은것이 우선
    global matrix, people, ei, ej, exited
    
    for length in range(1, N+1):
        for si in range(N-length+1):
            for sj in range(N-length+1):
                people_flag = False
                exit_flag = False
                for i in range(si, si+length):
                    for j in range(sj, sj+length):
                        # 출구 포함
                        if (i, j) == (ei, ej):
                            exit_flag = True
                        # 사람 포함
                        for num, (ci, cj) in people.items():
                            if exited[num]:
                                continue
                            if (i, j) == (ci, cj):
                                people_flag = True
                                break
                        if exit_flag and people_flag:
                            return si, sj, length
    return -1, -1, 0

def rotate_people(si, sj, length):
    global people

    temp_matrix = [[0] * length for _ in range(length)]

    for num, (ci, cj) in people.items():
        if exited[num]:
            continue
        x, y = ci - si, cj - sj
        if 0 <= x < length and 0 <= y < length:
            temp_matrix[x][y] = num

    temp_matrix = list(map(list, zip(*temp_matrix[::-1])))

    for i in range(length):
        for j in range(length):
            if temp_matrix[i][j] > 0:
                people[temp_matrix[i][j]] = (si+i, sj+j)

def rotate_exit(si, sj, length):
    global ei, ej
    temp_matrix = [[0] * length for _ in range(length)]

    x, y = ei - si, ej - sj

    temp_matrix[x][y] = 1
    temp_matrix = list(map(list, zip(*temp_matrix[::-1])))
    done = False
    for i in range(length):
        if done:
            break
        for j in range(length):
            if temp_matrix[i][j] == 1:
                ei, ej = (si + i, sj + j)
                done = True
                break


def rotate_matrix(si, sj, length):
    global matrix

    temp_matrix = [[0] * length for _ in range(length)]

    for i in range(length):
        for j in range(length):
            # 벽만 내구도 - 1
            if matrix[si+i][sj+j] > 0:
                temp_matrix[i][j] = matrix[si+i][sj+j] - 1
    # 판 회전
    temp_matrix = list(map(list, zip(*temp_matrix[::-1])))

    for i in range(length):
        for j in range(length):
            matrix[si + i][sj + j] = temp_matrix[i][j]
         

def rotate():
    # 3. 선택된 정사각형은 시계방향으로 90도 회전, 회전된 벽은 내구도 1 감소
    global matrix, people, ei, ej 

    si, sj, length = find_square()

    if length != 0:
        rotate_matrix(si, sj, length)
        rotate_people(si, sj, length)
        rotate_exit(si, sj, length)


res = 0
for k in range(K):
    # K초 전 모든 참가자 탈출
    if list(exited.values()).count(True) == M:
        break

    move_people()

    rotate()

print(sum(list(dist.values())))
print(ei+1, ej+1)



