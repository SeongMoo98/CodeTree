n = int(input())
a = [int(input()) for _ in range(n)]

# Please write your code here.
# 모든 사람이 같은 방에서 시작(시계 반대방향으로 이동)
# 어떤 방에서 시작해야 각 방에 정해진 인원이 들어가는 데까지의
# 거리의 합이 최소화하는가
a.extend(a)
min_dist = float('inf')
for start_room in range(n):
    move_dist = 0
    for i in range(n):
        visit_room = (start_room + i)
        move_dist += abs(visit_room - start_room) * a[visit_room]
    min_dist = min(min_dist, move_dist)

print(min_dist)