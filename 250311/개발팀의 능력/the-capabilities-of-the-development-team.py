# 개발자 5명의 알고리즘 능력이 정수로 주어짐
# 2명, 2명, 1명이 팀
# 최대 능력의 팀과 최소 능력의 팀과의 차이가 최소가 되도록
# 단, 모든 팀의 능력치 합이 서로 다르게 팀을 묶어야함

N = 5
scores = list(map(int, input().split()))
res = -1
for i in range(N-1):
    for j in range(i+1, N):
        team1 = scores[i] + scores[j]
        for k in range(N-1):
            for m in range(k+1, N):
                team2 = scores[k] + scores[m]
                tema3 = sum(scores) - team1 - team2
                if i != k and i != m and j != k and j != m and \
                    team1 != team2 and team2 != team3:
                    res = min(res, max(team1, team2, tema3) - min(team1, team2, tema3))

print(res)
                

