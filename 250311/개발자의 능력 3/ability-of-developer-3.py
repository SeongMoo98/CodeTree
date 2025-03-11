# 6명을 3명씩 2팀으로 배정
# 능력 총합간의 차이를 최소화 -> 차를 출력

scores = list(map(int, input().split()))

total_sum = sum(scores)
min_sub = float('inf')
for i in range(4):
    for j in range(1, 5):
        for k in range(2, 6):
            temp_sum = scores[i] + scores[j] + scores[k]
            min_sub = min(min_sub, abs((total_sum - temp_sum) - temp_sum))

print(min_sub)    


        