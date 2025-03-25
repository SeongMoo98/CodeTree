# 1 이상 4이하의 정수
# 정확히 해당 숫자만큼 연달아 같은 숫자가 나오면 아름다운수

# 1333221 : 1이 1번, 3이 3번, 2가 2번

# 111 : 1이 1번 나온 것이 3번 반복 -> 아름다운 수

# N자리 아름다운 수가 몇개 있는지 확인

N = int(input())

res = []
count = 0 
def backtrack():
    global res, count

    if len(res) == N:
        curr_num = res[0]
        curr_count = 1
        for idx in range(1, N):
            if curr_num == res[idx]:
                curr_count += 1
            else:
                # 숫자가 바뀜
                # 아름다운 수 x
                if curr_count % curr_num != 0:
                    return
                else:
                    curr_num = res[idx]
                    curr_count = 1
        if curr_count % curr_num ==0:
            count += 1
        return
    
    for i in range(1, 5):
        res.append(i)
        backtrack()
        res.pop()

backtrack()
print(count)
