N = int(input())

# x, y좌표
points = [tuple(map(int, input().split())) for _ in range(N)]

# 정확히 하나의 점만 뺀 후
# 모든 점들을 포함하는 직사각형의 넓이를 최소

left, right, top, down = 0, 0, 0, 0
area = 40000 * 40000

def find_points(points):
    x = [point[0] for point in points]
    y = [point[1] for point in points]

    left, right = min(x), max(x)
    down, top = min(y), max(y)

    return left, right, down, top

for i in range(N):
    temp = points.copy()
    temp.pop(i)
    l, r, d, t = find_points(temp)
    area = min(area, (r - l) * (t - d))
print(area)


