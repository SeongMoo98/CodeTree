# 코드트리 빵

# 빵을 구하고자 하는 사람 M명, 1번 사람은 1분에, 2번 사람은 2분에 ... 각자 베이스캠프에서 출발하여 편의점으로 이동
# 사람들은 출발 시간이 되기 전까지 격자 밖에 나와있으며, 사람들이 목표로하는 목표로 하는 편의점은 모두 다르다
# 총 몇 분후에 모두 편의점에 도착하는지 구하여라

# 각 사람마다 가고싶은 편의점의 위치는 겹치지 않으며, 편의점의 위치와 베이스캠프의 위치도 겹치지 않는다
# 어떠한 사람이 원하는 편의점에 도달하지 못하게 되는 경우는 절대 발생하지 않는다.
# 이동하는 도중 동일한 칸에 둘 이상의 사람이 위치하게 되는 경우도 가능하다

from collections import deque
# 격자 크기 N, 사람 수 M
# N <= 15, M <= 30
N, M = map(int, input().split())

# 격자 정보
# 0은 빈공간, 1은 베이스 캠프
matrix = [[0] * N for _ in range(N)]
# 갈 수 있는지 check 하는 Matrix
can_go = [[True] * N for _ in range(N)]

# 사람
people = [(0, 0)] * M
# 가고 싶어하는 편의점
conv = [(0, 0)] * M
success = [False] * M
basecamp = []

INF = float('inf')

for i in range(N):
    temp = list(map(int, input().split()))
    for j in range(N):
        if temp[j] == 1:
            basecamp.append((i, j))
        matrix[i][j] = temp[j]

# 각 사람들이 가고자 하는 편의점의 위치
for i in range(M):
    x, y = map(lambda x : int(x)-1, input().split())
    conv[i] = (x, y)


def is_range(x, y):
    return 0 <= x < N and 0 <= y < N


def people_bfs(si, sj, ei, ej):
    q = deque([(si, sj)])
    visited = [[(-1, -1)] * N for _ in range(N)]
    visited[si][sj] = (si, sj)
    while q:
        ci, cj = q.popleft()

        # 편의점 도착
        if (ci, cj) == (ei, ej):
            path = [(ei, ej)]
            ci, cj = ei, ej
            while True:
                if (ci, cj) == (si, sj):
                    # path[-1]은 시작점, path[-2]은 그 다음음
                    return path[-2]
                ni, nj = visited[ci][cj]
                path.append((ni, nj))
                ci, cj = ni, nj

        # 상, 좌, 우, 하
        for di, dj in [(-1, 0), (0, -1), (0, 1), (1, 0)]:
            ni, nj = ci + di, cj + dj
            if is_range(ni, nj) and can_go[ni][nj] == True and visited[ni][nj] == (-1, -1):
                q.append((ni, nj))
                visited[ni][nj] = (ci, cj)
    return (sj, sj)

def move_people(t):
    global people
    # 1. 격자에 있는 사람들 모두 본인이 가고 싶은 편의점 방향을 향해서 1칸 움직임
    #    최단거리로 움직이며, 상, 좌, 우, 하의 우선순위를 가지고 움직인다.
    #    최단거리 : 상하좌우 인접한 칸 중 이동가능한 칸으로만 이동하며, 도달하기기까지 거쳐야하는 칸의 수가 최소가 되는 거리
    if t >= M:
        t = M
    for i in range(t):
        # 이미 이동 완료한 사람은 건너뛰기
        if success[i] == True:
            continue
        ci, cj = people[i]
        ei, ej = conv[i]
        people[i] = people_bfs(ci, cj, ei, ej)

def arrive_conv(t):
    # 2. 편의점에 도착하면, 해당 편의점에서 멈추고, 이때부터 다른 사람들은 해당 편의점이 있는 칸을 지나갈 수 없다.
    #    격자에 있는 사람들이 모두 이동한 뒤에 해당 칸을 지나갈 수 없다(즉, 해당 1분이 지나고)
    global people, conv, can_go
    if t >= M:
        t = M

    for i in range(t):
        if success[i] == True:
            continue
        if people[i] == conv[i]:
            success[i] = True
            can_go[people[i][0]][people[i][1]]  = False


def conv_bfs(si, sj, ei, ej):
    global can_go
    q = deque([(si, sj)])
    visited = [[(-1, -1)] * N for _ in range(N)]
    visited[si][sj] = (si, sj)

    while q:
        ci, cj = q.popleft()
        # 편의점 도착
        if (ci, cj) == (ei, ej):
            path = [(ei, ej)]
            ci, cj = ei, ej
            while True:
                if (ci, cj) == (si, sj):
                    return len(path)-1
                ni, nj = visited[ci][cj]
                path.append((ni, nj))
                ci, cj = ni, nj

        for di, dj in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            ni, nj = ci + di, cj + dj
            if is_range(ni, nj) and can_go[ni][nj] == True and visited[ni][nj] == (-1, -1):
                q.append((ni, nj))
                visited[ni][nj] = (ci, cj)
    
    # 갈 수 있는 경로 x
    return INF


def add_people(t):
    global conv, basecamp, people, can_go
    # 3. 현재 시간이 t이고 t <= m을 만족한다면, t번 사람은 자신이 가고 싶은 편의점과 가장 가까이 있는 베이스 캠프에 들어간다.
    #    가장 가까운 베이스 캠프 : 1번과 같은 최단 거리 기준
    #    가장 가까운 베이스 캠프가 여러개라면 행이 작은, 열이 작은 의 우선순위로 베이스캠프로 돌아간다.
    #    t번 사람이 베이스 캠프로 이동하는데에 시간은 걸리지 않는다
    #    이때부터 다른 사람들은 해당 베이스캠프가 있는 칸을 지나갈 수 없다.

    #    t번 사람이 편의점을 향해 움직이기 시작했더라도 해당 베이스 캠프틑 절대 지나갈 수 없다
    #    마찬가지로, 해당 턴 격자에 있는 사람들이 모두 이동한 뒤에 해당 칸을 지나갈 수 없다

    # t번째 사람이 가려는 편의점
    ei, ej = conv[t]
    
    basecamp_res = []
    for si, sj in basecamp:
        if can_go[si][sj] == True:
            count = conv_bfs(si, sj, ei, ej)
            basecamp_res.append((count, si, sj))
    # count 작고, 행 작고, 열 작은
    basecamp_res.sort()

    # 베이스 캠프 선택
    selected_basecamp = basecamp_res[0]
    # 사람 베이스 캠프로 이동
    people[t] = (selected_basecamp[1], selected_basecamp[2])
    # 해당 칸은 지나갈 수 없게 처리
    can_go[selected_basecamp[1]][selected_basecamp[2]] = False


t = 0
while True:
    # 모두 편의점에 도착
    if success.count(True) == M:
        break

    # 1. 격자에 있는 사람들 움직임
    move_people(t)

    # 2. 편의점 도착 처리
    arrive_conv(t)

    # 3. 베이스 캠프에 추가
    if t < M:
        add_people(t)
    t += 1

print(t)