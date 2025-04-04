# 4 x 4 격자 
# M개의 몬스터, 1개의 팩맨

# M개의 몬스터는 상하좌우, 대각선 방향 중 하나를 가진다

# ************** 한턴 **************#
# 1. 몬스터 복제 시도
# 몬스터는 현재 위치에서 자신과 같은 방향을 가진 몬스터를 복제
# 알이 부화할 당시 해당 방향을 지닌채로 깨어남

# 2. 몬스터 이동
# 현재 자신이 가진 방향대로 한칸 이동
# 시체가 있거나, 팩맨이 있거나, 격자를 벗어날 경우 반시계 방향으로 45도 회전
# 갈 수 있는 경우가 없다면 움직이지 않는다

# 3. 팩맨 이동
# 팩맨은 3칸 이동(상하좌우)
# 이 중 몬스터를 가장 많이 먹을 수 있는 방향으로 움직인다
# 상 - 좌 - 하 - 우의 우선순위를 가진다
# 격자 바깥을 나가는 경우는 없다
# 팩맨을 알은 먹지 않고, 움직이기 전에 함께 있던 몬스터도 먹지 않는다

# 4. 몬스터 시체 소멸
# 몬스터의 시체는 총 2턴동안만 유지

# 5. 몬스터 복제 완성
# 알 형태의 몬스터 부화(방향은 복제가 된 몬스터 방향)

# Matrix에 여러개의 시체, 여러개의 알, 여러개의 몬스터가 존재할 수 있다.


N = 4

# 몬스터 수, 진행 턴 수
M, T = map(int, input().split())
# 팩맨의 초기 위치
pi, pj = map(lambda x : int(x)-1, input().split())

# 몬스터의 위치, 방향
# 0 ~ 7 : 상, 좌상, 좌, 좌하, 하, 우하, 우, 우상
num_of_monsters = M
monsters = {}
for num in range(1, M+1):
    mi, mj, d = map(lambda x : int(x)-1, input().split())
    monsters[num] = [(mi, mj), d]

# 복제된 monster : (num, d)
copy_monsters = [[[], [], [], []],
                [[], [], [], []],
                [[], [], [], []],
                [[], [], [], []]]
# 죽은 monster : (turn)
dead_monsters = [[[], [], [], []],
                [[], [], [], []],
                [[], [], [], []],
                [[], [], [], []]]

# 0 ~ 7 : 상, 좌상, 좌, 좌하, 하, 우하, 우, 우상
directions = {
    0 : (-1, 0),
    1 : (-1, -1),
    2 : (0, -1),
    3 : (1, -1),
    4 : (1, 0),
    5 : (1, 1),
    6 : (0, 1),
    7 : (-1, 1)
}

def copy():
    # 1. 몬스터 복제 시도
    # 몬스터는 현재 위치에서 자신과 같은 방향을 가진 몬스터를 복제
    # 알이 부화할 당시 해당 방향을 지닌채로 깨어남
    global copy_monsters, num_of_monsters

    for (mi, mj), d in monsters.values():
        copy_monsters[mi][mj].append((num_of_monsters+1, d))
        num_of_monsters += 1
    

def monster_move():
    global directions
    # 현재 자신이 가진 방향대로 한칸 이동
    # 시체가 있거나, 팩맨이 있거나, 격자를 벗어날 경우 반시계 방향으로 45도 회전
    # 갈 수 있는 경우가 없다면 움직이지 않는다
    for mon_num, [(mi, mj), d] in monsters.items():
        count = 0
        mon_d = d
        while True:
            if count == 8:
                break
            di, dj = directions[mon_d]
            ni, nj = mi + di, mj + dj
            # 범위 안, 시체 x, 팩맨 x, 
            if 0 <= ni < N and 0 <= nj < N and dead_monsters[ni][nj] == [] and (ni, nj) != (pi, pj):
                monsters[mon_num] = [(ni, nj), mon_d]
                break
            else:
                mon_d = (mon_d+1) % 8
                count += 1
    
def is_range(i, j):
    return 0 <= i < N and 0 <= j < N

def packman_move():
    global pi, pj, monsters, dead_monsters
    # 팩맨은 3칸 이동(상하좌우)
    # 이 중 몬스터를 가장 많이 먹을 수 있는 방향으로 움직인다
    # 상 - 좌 - 하 - 우의 우선순위를 가진다
    # 격자 바깥을 나가는 경우는 없다
    # 팩맨을 알은 먹지 않고, 움직이기 전에 함께 있던 몬스터도 먹지 않는다
    
    # 상, 좌, 하, 우
    packman_dir = {
        0: (-1, 0),
        1: (0, -1),
        2: (1, 0),
        3: (0, 1)
    }

    # 64개의 방향
    res = []
    for dir1 in range(4):
        ni1, nj1 = pi + packman_dir[dir1][0], pj + packman_dir[dir1][1]
        if not is_range(ni1, nj1):  continue
        for dir2 in range(4):
            ni2, nj2 = ni1 + packman_dir[dir2][0], nj1 + packman_dir[dir2][1]
            if not is_range(ni2, nj2):  continue
            for dir3 in range(4):
                ni3, nj3 = ni2 + packman_dir[dir3][0], nj2 + packman_dir[dir3][1]
                if not is_range(ni3, nj3):  continue

                eat = []
                for mon_num, [(mi, mj), d] in monsters.items():
                    if (ni1, nj1) == (mi, mj):
                        eat.append( (mon_num, (mi, mj)) )
                    # 이미 먹은것 포함 x
                    if (ni2, nj2) == (mi, mj) and (mon_num, (mi, mj)) not in eat:
                        eat.append( (mon_num, (mi, mj)) )
                    if (ni3, nj3) == (mi, mj) and (mon_num, (mi, mj)) not in eat:
                        eat.append( (mon_num, (mi, mj)) )
                count = len(eat)
                if count != 0:
                    res.append((count, dir1, dir2, dir3, eat))

    res.sort(key=lambda x:(-x[0], x[1], x[2], x[3]))                
    count, dir1, dir2, dir3, eat = res[0]
    pi = pi + packman_dir[dir1][0] + packman_dir[dir2][0] + packman_dir[dir3][0]
    pj = pj + packman_dir[dir1][1] + packman_dir[dir2][1] + packman_dir[dir3][1]

    for mon_num, (mi, mj) in eat:
        dead_monsters[mi][mj].append(2)
        monsters.pop(mon_num)
            

def dead():
    # 몬스터의 시체는 총 2턴동안만 유지
    global dead_monsters
    for i in range(N):
        for j in range(N):
            if dead_monsters[i][j] == 0:
                continue
            else:
                for k in range(len(dead_monsters[i][j])):
                    if dead_monsters[i][j][k] > 0:
                        dead_monsters[i][j][k] -= 1
                # turn이 종료 되면 빈 칸으로
                if len(dead_monsters[i][j]) == dead_monsters[i][j].count(0):
                    dead_monsters[i][j] = []

def alive():
    global copy_monsters, monsters
    # 알 형태의 몬스터 부화(방향은 복제가 된 몬스터 방향)

    # copy_monsters[i][j] : [(num, d)]
    for i in range(N):
        for j in range(N):
            if copy_monsters[i][j] == []:
                continue
            else:
                for k in range(len(copy_monsters[i][j])):
                    mon_num, d = copy_monsters[i][j][k]
                    monsters[mon_num] = [(i, j), d]
                copy_monsters[i][j] = []


for t in range(T):
    # 몬스터 복제
    copy()
    # 몬스터 이동
    monster_move()
    # 팩맨 이동
    packman_move()
    # 시체 소멸
    dead()
    # 몬스터 부화
    alive()
print(len(monsters))
