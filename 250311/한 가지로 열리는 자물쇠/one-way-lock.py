# 1 ~ N을 중복해서 뽑아 총 3자리
# 한 자리라도 주어지는 조합과 거리가 2 이내이면 열린다


N = int(input())
combination = tuple(map(int, input().split()))

count = 0
for i in range(1, N+1):
    for j in range(1, N+1):
        for k in range(1, N+1):
            if (abs(combination[0] - i) <= 2) or \
            (abs(combination[1] - j) <= 2)\
             or (abs(combination[2] - k) <= 2):
             count += 1
print(count)

