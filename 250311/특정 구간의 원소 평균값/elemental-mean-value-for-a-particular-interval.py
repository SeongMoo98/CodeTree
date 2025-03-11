N = int(input())
arr = list(map(int, input().split()))


# 특정 구간을 잡았을 때, 
# 그 구간 안에 있는 원소들의 평균값이 그 구간의 원소 중 하나가 되게하는 서로 다른 가짓수

# 1개, 2개 .. N개의 원소를 선택
count = 0
for inter in range(1, N+1):
    for j in range(N-inter+1):
        # inter개 선택
        temp = arr[j: j+inter]
        if sum(temp) / inter in temp:
            count += 1

print(count)