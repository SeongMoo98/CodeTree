# 수직선상의 N개의 선분이 주어졌을 때, 
# 서로 겹치지 않고 고를 수 있는 가장 많은 선분의 수
# 끝점을 겅유하는 것 역시 겹친 것

N = int(input())
lines = [list(map(int, input().split())) for _ in range(N)]

res = 0
selected_lines = []

def overlapped(line1, line2):
    l1, r1 = line1
    l2, r2 = line2

    # 겹치는지 판단
    return (l1 <= l2 <= r1) or \
           (l1 <= r2 <= r2) or \
           (l2 <= l1 <= r2) or \
           (l2 <= r1 <= r2)

def possible():
    for i, line1 in enumerate(selected_lines):
        for j, line2 in enumerate(selected_lines):
            # 겹치는지 안겹치는지 확인
            # line이 같지 않고 안겹칠 때
            if i < j and overlapped(line1, line2):
                return False
    return True

def backtrack(cnt):
    global res

    if cnt == N:
        if possible():
            res = max(res, len(selected_lines))
        return

    selected_lines.append(lines[cnt])
    backtrack(cnt+1)
    selected_lines.pop()

    backtrack(cnt+1)

backtrack(0)
print(res)