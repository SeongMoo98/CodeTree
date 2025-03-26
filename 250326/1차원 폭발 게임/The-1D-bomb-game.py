# N개의 폭탄이 쌓여있다.

# 이 떄, M개 이상 연속으로 같은 숫자가 적혀있는 폭탄들은 터지게 되고
# 중력에 의해 밑으로 떨어지게 된다.

# M개 이상 연속한 숫자를 갖는 폭탄들이 존재하지 않을 때까지 반복

N, M = map(int, input().split())
bombs = [int(input()) for _ in range(N)]

def check(bombs):
    n = len(bombs)
    curr_num = bombs[0]
    count = 1

    if count >= M:
        remove_idx = [0]
    else:
        remove_idx  = []

    for i in range(1, n):
        if curr_num == bombs[i]:
            count += 1
        # 같지 않다면 count를 확인해서 bomb
        else:  
            if count >= M:
                # 현재 i 번째 원소 이전부터 count개 만큼 없앰
                for idx in range(i-1, i-1-count, -1):
                    remove_idx.append(idx)
            curr_num = bombs[i]
            count = 1
    # 마지막 원소 처리
    if count >= M:
        for idx in range(n-1, n-1-count, -1):
            remove_idx.append(idx)

    removed_bomb = []
    for i in range(n):
        if i in remove_idx:
            continue
        removed_bomb.append(bombs[i])
    return removed_bomb

while True:
    removed_bomb = check(bombs)

    # 더이상 변화 x
    if removed_bomb == bombs or removed_bomb == []:
        break

    bombs = removed_bomb

print(len(removed_bomb))
for i in range(len(removed_bomb)):
    print(removed_bomb[i])


        
