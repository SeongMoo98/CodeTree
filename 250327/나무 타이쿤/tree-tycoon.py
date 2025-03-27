# 나무 리브로수를 N x N 격자에 키우고자 한다.

# N x N 격자에 서로 다른 높이를 가진 나무가 주어진다.

# 특수 영양제
# 1x1땅에 있는 나무의 높이를 1 증가시키며, 해당 땅에 씨앗만 있는 경우 높이 1의 나무를 만들어 냄

# 초기 영양제는 N x N 격자의 좌하단 4칸(2x2)에 주어진다.

# 각각의 영양제는 1~8번까지 방향으로 이동한다.(각 행,열은 끝과 끝이 연결되어 있다.)
# 우, 우상, 상, 좌상, 좌, 좌하, 하, 우하

# 성장 과정
# 1. 특수 영양제를 이동 규칙에 따라 이동시킴
# 2. 이동 시킨 후 땅에 영양제 투입(영양제 없어짐)
# 3. 특수 영양제를 투입한 리브로수의 대각선으로 인접한 방향에 
#    높이가 1이상의 리브로수가 있는 만큼 높이가 더 성장
#    (대각선으로 인접한 방향이 격자를 벗어나는 경우는 생략)
# 4. 영양제를 투입한 리브로수를 제외하고 
#    높이가 2이상인 리브로수는 높이를 2 베어서 잘라낸 리브로수로 
#    특수영양제를 사고 해당 위치에 특수 영양제를 올려놓음


# arr : 0은 씨앗만 존재, 0보다 크면 높이
# m개의 줄에 각 년도 이동규칙이 주어짐
# d, p : 이동 방향, 이동 칸 수

# 격자 크기, 년수
N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
# 초기 영양제 좌표
supplements = [[N-1, 0], [N-1, 1], [N-2, 0], [N-2, 1]]


directions = {
    1: (0, 1),
    2: (-1, 1),
    3: (-1, 0),
    4: (-1, -1),
    5: (0, -1),
    6: (1, -1),
    7: (1, 0),
    8: (1, 1)
}
def supplement_move(supplements, d, p):
    di, dj = directions[d]
    for supplement in supplements:
        supplement[0] = (supplement[0] + p * di) % N
        supplement[1] = (supplement[1] + p * dj) % N

    return supplements

def grow(supplements):
    global arr
    for supplement in supplements:
        ci, cj = supplement
        arr[ci][cj] += 1

    # 3. 대각선 방향 높이 1이상의 수만큼 추가 성장
    for supplement in supplements:
        ci, cj = supplement
        count = 0
        
        for di, dj in [(-1, -1), (-1, 1), (1, -1), (1, 1)]:
            ni, nj = ci + di, cj + dj
            if 0 <= ni < N and 0 <= nj < N and arr[ni][nj] >= 1:
                count += 1
        arr[ci][cj] += count
    

for _ in range(M):
    d, p = map(int, input().split())

    # 1. 영양제 이동
    # 좌표 넘어가도 이동
    supplements = supplement_move(supplements, d, p)
    # 2. 영양제 주사
    grow(supplements)
    
    # # 4. 높이 2 이상의 리브로수 팔기, 영양제 추가
    # 높이 2 이상의 영양제 좌표
    supplements_up_two = []
    for i in range(N):
        for j in range(N):
            if [i, j] not in supplements and arr[i][j] >= 2:
                arr[i][j] -= 2
                supplements_up_two.append([i, j])
    # 현재 영양제 좌표를 버리고(이미 썼기때문에)
    # 새로운 영양제 좌표
    supplements = supplements_up_two

res = 0
for i in range(N):
    for j in range(N):
        res += arr[i][j]
print(res)




