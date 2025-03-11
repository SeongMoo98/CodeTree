# N개의 밭의 높이가 주어질때
# 연속하게 T번 이상 H 높이로 나오게끔 하려고 할 때 최소비용

N, H, T = map(int, input().split())
heights = list(map(int, input().split()))

min_sum = float('inf')

for i in range(N - T + 1):
    temp = heights[i:i+T]
    h = 0
    for j in range(T):
        h += abs(H - temp[j])
    min_sum = min(min_sum, h)
print(min_sum)