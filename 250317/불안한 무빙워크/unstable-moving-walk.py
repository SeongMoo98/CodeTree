# 길이가 N인 무빙워크
# 무빙워크 : 사람을 한쪽 끝에서 반대쪽 끝으로 옮겨주는 기계(길이 2N)

# 무빙워크의 레일은 시계방향으로 회전
# 1 ~ 2N-1 : 2N번째 칸으로 이동
# 2N : 1번째 칸으로 이동

# 각 사람은 1번 칸에 올라서서 N번 칸에서 내린다
# 사람이 칸에 올라가거나 이동하면 그 칸의 안정성은 즉시 1만큼 감소(0이면 올라갈 수 없다)

# 1. 무빙워크 1칸 회전
# 2. 가장 먼저 무빙워크에 올라간 사람부터 무빙워크가 회전하는 방향으로 한칸 이동할 수 있으면 이동
#    만약 앞선 칸에 사람이 있거나 앞선 칸의 안정성이 0이면 이동 x
# 3. 1번 칸에 사람이 없고 안정성이 0이 아니라면 사람을 한명 더 올림
# 4. 안정성이 0인 칸이 k개 이상이면 과정 종료

# 1 ~ 3 과정 중 N번 칸에 사람이 위치하면 그 즉시 내린다.

# 위의 과정이 1번의 실험이라고 할 때, 과정이 종료될 때 몇번 째 실험을 하고 있는지 구하여라

from collections import deque

# N : 무빙워크 길이, K : 0인 판의 개수
N, K = map(int, input().split())
# 무빙워크의 안정성
# 1 ~ 2N
safety = [-1] + list(map(int, input().split()))
# [0] : 제일 먼저 올라간 사람
people = deque([])
turn = 0

out = False
while safety[1:].count(0) < K:
    # 1. 무빙워크 회전
    # 2N번째 칸 저장  
    temp = safety[-1]
    safety[2:] = safety[1:2*N]
    safety[1] = temp
    # 사람도 같이 이동
    if people:
        for i in range(len(people)):
            people[i] += 1
            if people[i] == N:
                out = True

    if out:
        people.popleft()
        out = False


    # 2. 무빙워크가 회전하는 방향으로 한칸 이동
    if people:
        for i in range(len(people)):
            # 사람이 없거나, 안정성이 0이 아닐때
            curr = people[i]
            if (curr + 1) not in people and safety[curr+1] > 0:
                people[i] += 1
                # 이동한 칸의 안정성 -1
                safety[curr+1] -= 1   
                
                # N번쨰 위치면 내림
                # 근데 내리는 사람은 결국 맨 앞에 있는 사람
                if people[i] == N:
                    out = True
    if out:
        people.popleft()
        out = False    

    # 3. 1번칸에 사람 없으면 사람 올림
    if 1 not in people and safety[1] > 0:
        people.append(1)
        safety[1] -= 1
    turn += 1
print(turn)




