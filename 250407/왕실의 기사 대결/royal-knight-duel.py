'''
왕실의 기사 대결

L x L 체스판 위에서 대결 준비(빈칸, 함정, 벽, 체스판 밖도 벽)

기사
마력으로 상대방을 밀쳐냄
(r, c)를 좌측 상단으로 하여 h x w 크기의 직사각형 형태의 방패, 체력 k

1. 기사 이동
    명령받은 기사는 상하좌우 한칸 이동
    다른 기사가 있으면 한 칸씩 민다
    만약 이동하려는 방향 끝에 벽이 있으면 모든 기사 이동 x
    체스판에서 사라진 기사에게 명령 x

2. 대결 데미지
    명령을 받은 기사가 다른 기사를 밀치게 되면, 밀려난 기사들이 피해를 입는다.
    각 기사들은 해당 기사가 이동한 곳에서 h x w 직사각형 내에 놓여있는 함정의 수 만큼 피해를 받음
    각 기사는 피해를 받은 만큼 체력이 깎임(현재 체력이상의 데미지를 받으면 체스판에서 사라짐)
    단, 명령을 받은 기사는 피해 x, 또한 기사들이 모두 밀린 이후에 데미지 적용
    (밀렸더라도 직사각형 내에 함정이 없다면 그 기사는 피해 x)

Q번에 걸쳐 왕의 명령이 주어졌을 때, Q번의 대결이 끝난 후 생존한 기사들이 받은 총 데미지


체스판의 크기 L, 기사의 수 N, 명령의 수 Q
3 <= L <= 40, 1 <= N <= 30, 1 <= Q <= 100
시간복잡도는 적당하다

초기 기사의 위치는 겹치지 않는다. 또한, 기사와 벽은 겹쳐서 주어지지 않는다.
'''
from collections import deque
L, N, Q = map(int, input().split())

# 빈칸 :0 , 함정 : 1, 벽 : 2 (격자 밖도 벽처리)
matrix = [list(map(int, input().split())) for _ in range(L)]

knight_pos = dict()
# 현재 체력
hp = [0] * (N+1)
# 현재 받은 데미지
damage = [0] * (N+1)
alive = [True] * (N+1)

# 초기 기사들의 정보
for num in range(1, N+1):
    # 1번 기사부터 N번 기사까지 순서대로
    r, c, h, w, k = map(int, input().split())
    # 좌상단 좌표
    r, c = r-1, c-1
    knight = []
    for i in range(h):
        for j in range(w):
            knight.append((r+i, c+j))
    knight_pos[num] = knight
    hp[num] = k

# d : 상, 우, 하, 좌(0 ~ 3)
directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]


def move_knight(knight_num, d):

    temp_matrix = [[0] * L for _ in range(L)]
    # 임시 Matrix에 기사 번호 기록
    for num, pos_list in knight_pos.items():
        for ci, cj in pos_list:
            temp_matrix[ci][cj] = num

    fight_list = [knight_num]

    q = deque([knight_num])
    di, dj = directions[d]

    # while로 돌면서 현재 knight의 모든 point를 d방향으로 밀었을때
    # matrix에서 다른 숫자를 만나면 부딪히는 list에 추가
    # 계속 돌면서 벽을 만나거나, 범위 밖이면 바로 종료(빈리스트)
    while q:
        curr_knight = q.popleft()

        for ci, cj in knight_pos[curr_knight]:
            ni, nj = ci + di, cj + dj
            # 하나라도 범위 밖이거나, 하나라도 벽을 만나면 종료
            if (ni < 0 or ni >= L or nj < 0 or nj >= L) or matrix[ni][nj] == 2:
                return []
            # 다른 기사를 만나면 fight_list에 추가
            if temp_matrix[ni][nj] != 0 and temp_matrix[ni][nj] not in fight_list:
                q.append(temp_matrix[ni][nj])
                fight_list.append(temp_matrix[ni][nj])
    return fight_list


for _ in range(Q):
    # i(1 ~ N)번째 기사에서 방향 d를 준다(이미 사라진 기사의 번호를 줄 수도 있다.)
    Q_num, Q_d = map(int, input().split())

    if alive[Q_num] == False:
        continue

    # # [1] 명령받은 기사 이동(어떤 기사들이 이동하는지 확인)
    fight_list = move_knight(Q_num, Q_d)


    # [2] 기사 이동 처리
    # [1]에서 범위 내, 벽 여부 왁인 함
    if fight_list:  # 움직이는 기사 번호들
        di, dj = directions[Q_d]
        for knight_num in fight_list:
            for i in range(len(knight_pos[knight_num])):
                ci, cj = knight_pos[knight_num][i]
                knight_pos[knight_num][i] = (ci + di, cj + dj)

    # [3] 데미지 처리
    # 밀려난 곳에서 직사각형 내의 함정 개수만큼 피해

    if fight_list:
        for knight_num in fight_list:
            # 명령받은 기사는 제외, 죽은 기사도 제외
            if knight_num == Q_num or alive[knight_num] == False:
                continue
            cnt = 0
            for ci, cj in knight_pos[knight_num]:
                if matrix[ci][cj] == 1:
                    cnt += 1
            damage[knight_num] += cnt
            hp[knight_num] -= cnt

    for knight_num in range(1, N+1):
        if hp[knight_num] <= 0:
            alive[knight_num] = False

res = 0
for i in range(1, N+1):
    if alive[i]:
        res += damage[i]
print(res)