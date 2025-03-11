# 6명을 3명씩 2팀으로 배정
# 능력 총합간의 차이를 최소화 -> 차를 출력

scores = list(map(int, input().split()))

total_sum = sum(scores)

min_sub = float('inf')
for i in range(4):
    for j in range(i+1, 5):
        for k in range(j+1, 6):
            team1 = scores[i] + scores[j] + scores[k]
            team2 = total_sum - team1
            min_sub = min(min_sub, abs(team1 - team2))
            

print(min_sub)    


        