# 1 이상 K 이하의 수를 하나 고르는 행위를 N번 반복하여 나올 수 있는 서로 다른 모든 순서 쌍
# 단, 연속해서 같은 숫자가 3번 이상 나오는 경우는 제외


K, N = map(int, input().split())

def backtrack(res, count):
    global K, N

    if count >= 3:
        return 

    # 종료 조건
    if len(res) == N:
        for i in range(N):
            print(res[i], end=' ')
        print()
        return
    prev_count = 0
    for i in range(1, K+1):
        if res == []:
            count = 1
        else:
            if res[-1] == i:
                count += 1
            else:
                prev_count = count
                count = 1
        res.append(i)
        backtrack(res, count)
        res.pop()
        count = prev_count



backtrack([], 0)