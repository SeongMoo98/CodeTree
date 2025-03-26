# N x N 학생을 놀이기구에 순서대로 탑승시키려한다

# 각 학생별로 좋아하는 학생이 4명 있다(자기 자신을 좋아하는 학생 x, 중복도 x)

# 아래 조건에 따라 가장 우선순위가 높은 칸으로 탑승(비어있는 칸)

# 1. 4방향 인접한 칸 중, 좋아하는 친구의 수가 가장 많은 위치
# 2. 그런 곳이 여러 곳이면, 인접한 칸 중 비어있는 칸의 수가 가장 많은 위치
#      이동하려는 칸의 인접 4방향 비어있는 칸의 수
# 3. 여러 곳이면, 행번호가 작은 위치
# 4. 여러 곳이면, 열번호가 작은 위치

# 최종 점수
# 모든 학생이 탑승한 이후, 각 학생마다의 점수를 합한 점수
# 각 학생의 점수는 해당 학생의 인접한 곳에 앉아 있는 좋아하는 친구의 수
# 0명 : 0점, 1명 : 1점, 2명 : 10점, 3명 : 100점, 4명 : 1000점

from collections import defaultdict
N = int(input())
matrix = [[0] * N for _ in range(N)]

d = [(-1, 0), (1, 0), (0, -1), (0, 1)]
# 좋아하는 친구
friends = defaultdict(list)
# 탑승 순서
order = []
for _ in range(N*N):
    n0, n1, n2, n3, n4 = map(int, input().split())
    friends[n0] = [n1, n2, n3, n4]
    order.append(n0)
res = 0

def get_score():
    global res
    for i in range(N):
        for j in range(N):
            student_num = matrix[i][j]
            count = 0
            for di, dj in d:
                ni, nj = i + di, j + dj
                if 0 <= ni < N and 0 <= nj < N:
                    if matrix[ni][nj] in friends[student_num]:
                        count += 1
            if count != 0:
                res += 10 ** (count - 1)

def find_position(student_num, ci, cj):
    friend_count = 0
    blank_count = 0 
    for di, dj in d:    
        ni, nj = ci + di, cj + dj
        # 범위 내
        if 0 <= ni < N and 0 <= nj < N:
            if matrix[ni][nj] in friends[student_num]:
                friend_count += 1
            if matrix[ni][nj] == 0:
                blank_count += 1

    return (friend_count, blank_count, i, j)

for stu_num in order:
    candidates = []
    for i in range(N):
        for j in range(N):
            # 빈칸 일 때
            if matrix[i][j] == 0:
                candidates.append(find_position(stu_num, i, j))
    candidates.sort(key=lambda x: (-x[0], -x[1], x[2], x[3]))
    ei, ej = candidates[0][2], candidates[0][3]
    matrix[ei][ej] = stu_num
                

get_score()
print(res)


