# 팩맨
# 4 x 4 격자, m개의 몬스터, 1개의 팩맨
# 몬스터 : 상하좌우, 대각선 방향중 하나를 가짐

from collections import deque
# 몬스터 수, 턴 수
N = 4
M, T = map(int, input().split())

# 팩맨의 위치
pi, pj = map(lambda x:int(x)-1, input().split())
monsters = dict()
monsters_dir = dict()
monsters_num = M

# list 참조 문제
# 빈 리스트롤 곱하여서 사용하였기 때문에 4개의 빈 리스트라 해도 같은 주소 공유
# ==> 수정, 복사가 동일하게 나타남
dead_monsters = [
    [[], [], [], []],
    [[], [], [], []],
    [[], [], [], []],
    [[], [], [], []]
]
# d 기록록
copy_monsters = [
    [[], [], [], []],
    [[], [], [], []],
    [[], [], [], []],
    [[], [], [], []]
]
# 상, 좌상, 좌, 좌하, 하, 우하, 우, 우상
directions = {
    0: (-1, 0),
    1: (-1, -1),
    2: (0, -1),
    3: (1, -1),
    4: (1, 0),
    5: (1, 1),
    6: (0, 1),
    7: (-1, 1)
}
# 몬스터의 위치와 방향
for num in range(1, M+1):
    r, c, d = map(lambda x:int(x)-1, input().split())
    monsters[num] = [r, c]
    monsters_dir[num] = d


def monster_copy(monsters, monsters_dir,copy_monsters):
    # 몬스터는 현재 위치에서 자신과 같은 방향을 가진 몬스터를 복제하려 한다.
    # 이 때, 복제된 몬스터는 아직 부화되지 않은 상태로 움직이지 못한다.
    # 복제된 몬스터는 현재 시점을 기준으로 각 몬스터와 동일한 방향을 지니게 되며, 부화할 시 해당 방향을 지님
    for mon_num, (r, c) in monsters.items():
        copy_monsters[r][c].append(monsters_dir[mon_num])

    return copy_monsters

def monster_move(monsters, monsters_dir, pi, pj, dead_monsters):
    # 현재 자신이 가진 방향으로 1칸 이동
    # 움직이려는 칸에 시체가 있거나, 팩맨이 있는 경우거나, 격자를 벗어나는 방향의 경우 반시계 방향으로 45도 회전
    # 회전해도 갈 수 없다면, 가능할 때까지 반시계방향으로 45도 회전
    # 만약, 갈 수 있는 방향이 없다면 이동 x

    for mon_num, (mi, mj) in monsters.items():
        # 반시계 방향으로 회전
        for i in range(8-1):
            md = (monsters_dir[mon_num] + i) % 8
            ni, nj = mi + directions[md][0], mj + directions[md][1]

            # 격자안, 시체 x, 팩맨 x
            if 0 <= ni < N and 0 <= nj < N and dead_monsters[ni][nj] == [] and (ni, nj) != (pi, pj):
                monsters[mon_num] = [ni, nj]
                monsters_dir[mon_num] = md
                break
            else:
                continue
    return monsters, monsters_dir


def is_range(i, j):
    return 0 <= i < N and 0 <= j < N

def packman_move(pi, pj, monsters, monsters_dir, dead_monsters):
    # 3칸이동, 각 이동마다 상하좌우의 선택지를 가짐
    # 3칸을 이동할 때 64개의 선택지가 생기는데 이때, 몬스터를 가장 많이 먹을 수 있는 위치로 이동
    # 가장 많이 먹을 수 있는 방향이 여러개라면, (상, 좌, 하, 우) 순으로 우선순위를 가짐
    # 격자를 벗어나지 않는다.
    # 이 때, 이동할 때 이동하는 칸에 있는 몬스터는 모두 먹어치운 뒤, 몬스터는 시체가 남는다.
    # 또한, 알을 먹지 않으며, 움직이기 전에 함께 있던 몬스터도 먹지 않는다

    # 상, 좌, 하, 우
    packman_dir = {
        0 : (-1, 0),
        1 : (0, -1),
        2 : (1, 0),
        3 : (0, 1)
    }
    # (count, 3개의 방향, mon_nums)
    eat_monster = []
    # 3번 이동

    
    # while q:
    #     ci, cj = q.popleft()
    #     for pd in range(4):
    #         di, dj = packman_dir[pd]
    #         if 0 <= ni < N and 0 <= nj < N:
    #             # for mon_num, (mi, mj) in monsters.items():
    #             #     if (ni, nj) == (mi, mj):

    # 64개의 방향
    move_to = []
    for i in range(4):
        for j in range(4):
            for k in range(4):
                move_to.append((i, j, k))
    
    for d1, d2, d3 in move_to:
        count = 0
        di1, dj1 = packman_dir[d1]
        ni1, nj1 =  pi + di1, pj + dj1

        di2, dj2 = packman_dir[d2]
        ni2, nj2 =  ni1 + di2, nj1 + dj2

        di3, dj3 = packman_dir[d3]
        ni3, nj3 =  ni2 + di3, nj2 + dj3

        # 3번의 이동이 모두 범위 내
        if is_range(ni1, nj1) and is_range(ni2, nj2) and is_range(ni3, nj3):
            if [ni1, nj1] in monsters.values():
                count += list(monsters.values()).count([ni1, nj1])
            
            if [ni2, nj2] in monsters.values() and (pi, pj) != (ni2, nj2):
                count += list(monsters.values()).count([ni2, nj2])

            if [ni3, nj3] in monsters.values() and (ni1, nj1) != (ni3, nj3):
                count += list(monsters.values()).count([ni3, nj3])
       
        eat_monster.append([count, d1, d2, d3])

    # d1, d2, d2는 상, 좌, 하, 우 순으로 0, 1, 2, 3이니
    # 오름차순 정렬
    eat_monster.sort(key=lambda x: (-x[0], x[1], x[2], x[3]))
    c, d1, d2, d3 = eat_monster[0]

    di1, dj1 = packman_dir[d1]
    ni1, nj1 =  pi + di1, pj + dj1

    di2, dj2 = packman_dir[d2]
    ni2, nj2 =  ni1 + di2, nj1 + dj2

    di3, dj3 = packman_dir[d3]
    ni3, nj3 =  ni2 + di3, nj2 + dj3

    remove_mon = []
    for mon_num, (mi, mj) in monsters.items():
        if (mi, mj) == (ni1, nj1):
            remove_mon.append(mon_num)
        
        if (mi, mj) == (ni2, nj2):
            remove_mon.append(mon_num)

        if (mi, mj) == (ni3, nj3):
            remove_mon.append(mon_num)
    
    for remove_num in remove_mon:
        if remove_num in monsters.keys():
            mi, mj = monsters[remove_num]
            monsters.pop(remove_num)
            monsters_dir.pop(remove_num)
            
            dead_monsters[mi][mj].append(2)
            

    pi, pj = ni3, nj3

    return pi, pj, monsters, monsters_dir, dead_monsters

    

def monster_dead(dead_monsters):
    # 몬스터의 시체는 총 2턴동안 유지
    # 시체가 생기고 나면, 시체가 소멸되기 까지는 총 두턴이 픨요
    for i in range(N):
        for j in range(N):
            if dead_monsters[i][j] == []:
                continue
            else:
                for k in range(len(dead_monsters[i][j])):
                    if dead_monsters[i][j][k] > 0:
                        dead_monsters[i][j][k] -= 1
                for k in range(len(dead_monsters[i][j])):
                    if dead_monsters[i][j][k] > 0:
                        break
                else:
                    dead_monsters[i][j] = []
                    
                
    return dead_monsters

def monster_alive(monsters_num, copy_monsters):
    # 알 형태의 몬스터가 부화(처음 복제된 몬스터의 방향을 지닌 채로 깨어남)
    for i in range(N):
        for j in range(N):
            if copy_monsters[i][j] == []:
                continue
            else:
                for k in range(len(copy_monsters[i][j])):
                    monsters_num += 1
                    monsters[monsters_num] = [i, j]
                    monsters_dir[monsters_num] = copy_monsters[i][j][k]
                copy_monsters[i][j] = []

    return monsters_num, copy_monsters


for t in range(T):
    # 1. 몬스터 복제 시도
    copy_monsters = monster_copy(monsters, monsters_dir, copy_monsters)
    # 2. 몬스터 이동
    monsters, monsters_dir = monster_move(monsters, monsters_dir, pi, pj, dead_monsters)
    # 3. 팩맨 이동
    pi, pj, monsters, monsters_dir, dead_monsters = packman_move(pi, pj, monsters, monsters_dir, dead_monsters)
    # 4. 몬스터 시체 소멸
    dead_monsters = monster_dead(dead_monsters)
    # 5. 몬스터 복제 완성
    monsters_num, copy_monsters = monster_alive(monsters_num, copy_monsters)


# 모든 턴이 진행되고 난 뒤 살아 남아 있는 몬스터의 마리 수 출력
print(len(monsters))