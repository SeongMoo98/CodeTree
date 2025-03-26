# N개의 층으로 이루어진 1차원 젠가

# 2번에 걸쳐 특정 구간의 블럭들을 뺴는 작업 
# 남은 블럭은 중력에 의해 떨어져 남게된다.

N = int(input())

blocks = [0] + [int(input()) for _ in range(N)]

for _ in range(2):
    # start ~ end 블록 제거
    # 나머지는 중력에 의해 아래로 이동
    start, end = map(int, input().split())
    temp = []
    for i in range(1, len(blocks)):
        if start <= i <= end:
            continue
        temp.append(blocks[i])
    blocks = [0]
    for num in temp:
        blocks.append(num)
    

if len(temp) == 0:
    print(0)
else:
    print(len(temp))
    for i in range(len(temp)):
        print(temp[i])

