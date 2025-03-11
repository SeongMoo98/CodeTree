# 6명을 3명씩 2팀으로 배정
# 능력 총합간의 차이를 최소화 -> 차를 출력

scores = list(map(int, input().split()))

total_sum = sum(scores)

min_sub = float('inf')
res = 0
for i in range(4):
    for j in range(1, 5):
        for k in range(2, 6):
            team1 = scores[i] + scores[j] + scores[k]
            team2 = total_sum - team1
            if abs(team1 - team2) < min_sub:
                min_sub = abs(team1 - team2)
                res = abs(team1 - team2)
            

print(res)    


        