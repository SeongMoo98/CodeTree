# 1 ~ 100으로 이루어진 N x N 격자

# 임의의 기울어진 정사각형을 잡아 회전
# 격자내에 있는 한 지점으로부터 반시계(시계) 순회를 했을 때 지나왔던 지점들의 집합

# 1, 2, 3, 4번 방향순으로 순회(우상, 좌상, 좌하, 우하)
# 이동하는 도중 격자 밖으로 나가면 안됨
# 각 대각선의 길이가 다를 수 있다.

# 기울어진 사각형에 대해 반시계 혹은 시계방향으로 회전해야하는 정보가 주어졌을때
# 회전 이후 결과 출력

N = int(input())

arr = [list(map(int,input().split())) for _ in range(N)]

# 직사각형의 정보와 회전방향

# r행 c열에서 출발
# 1번, 2번, 3번, 4번 방향으로 m1, m2, m3, m4만큼 순서대로 이동했을떄
# dir=0 : 반시계, dir=1 : 시계
r, c, m1, m2, m3, m4, direction = map(int, input().split())
si, sj = r-1, c-1

# 반시계 : 우상, 좌상, 좌하, 우하
if direction == 0:
    
    d = [(-1, 1), (-1, -1), (1, -1), (1, 1)]
    ms = [m1, m2, m3, m4]
# 시계 : 좌상, 우상, 우하, 좌하
else:
    d = [(-1, -1), (-1, 1), (1, 1), (1, -1)]
    ms = [m4, m3, m2, m1]

moving_idx = [(si, sj)]
moving_num = [arr[si][sj]]
ci, cj = si, sj

for m, (di, dj) in zip(ms, d):
    for _ in range(m):
        ni, nj = ci+di, cj+dj
        if 0<=ni<N and 0<=nj<N:
            moving_idx.append((ni, nj))
            moving_num.append(arr[ni][nj])
            ci, cj = ni, nj

temp = moving_num[-1]
moving_num[1:] = moving_num[0:len(moving_num)-1]
moving_num[0] = temp

for num, (i, j) in zip(moving_num, moving_idx):
    arr[i][j] = num

for i in range(N):
    for j in range(N):
        print(arr[i][j], end=' ')
    print()
