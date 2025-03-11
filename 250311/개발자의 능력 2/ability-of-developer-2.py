# 6명을 2명씩 3팀으로 배정

# 팀원들의 능력 총합이 가장 큰 팀과 가장 작은 팀의 차이를 최소화할 때
# 최대팀과 최소 팀간의 차를 출력
scores = map(int, input().split())
total_sum = sum(scores)
min_sub = float("inf")
for i in range(3):
    for j in range(i+1, 4):
        team1 = scores[i] + scores[j]
        for l in range(j+1, 5):
            for m in range(l+1, 6):
                team2 = scores[l] + scores[m]
                team3 = total_sum - team1 - team2
                max_team = max(team1, team2, team3)
                min_team = min(team1, team2, team3)
                min_sub = min(min_sub, max_team - min_team)
print(min_sub)