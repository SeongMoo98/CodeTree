# 6명을 2명씩 3팀으로 배정

# 팀원들의 능력 총합이 가장 큰 팀과 가장 작은 팀의 차이를 최소화할 때
# 최대팀과 최소 팀간의 차를 출력
n = 6
scores = list(map(int, input().split()))
total_sum = sum(scores)

min_sub = float("inf")
for i in range(n):
    for j in range(i+1, n):
        # 얘는 왜 0부터 시작인가?
        # (i, j)가 (0,2)일 때 (l, m)은 (1, 3)이 가능하기 때문이다
        for l in range(n):
            for m in range(l+1, n):
                if l != i and l != j and m != i and m != j:
                    team1 = scores[i] + scores[j]
                    team2 = scores[l] + scores[m]
                    team3 = total_sum - team1 - team2
                    min_sub = min(min_sub, max(team1, team2, team3) - min(team1, team2, team3))
print(min_sub)