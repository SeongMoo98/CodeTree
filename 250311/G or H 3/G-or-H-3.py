n, k = map(int, input().split())
x = []
c = []
# N명이 위치 x에서 G, H를 받음
# G는 1, H는 2
# 사진의 크기가 K
for _ in range(n):
    pos, char = input().split()
    x.append(int(pos))
    c.append(char)

# Please write your code here.

max_x = max(x)
# 위치는 1 ~ x
positions = [0] * (max_x + 1) 

for pos, ch in zip(x, c):
    positions[pos] = ch

max_score = 0
for i in range(max_x-k+1):
    score = 0
    temp = positions[i:i+k+1]
    score += temp.count("G")
    score += 2 * temp.count("H")
    
    max_score = max(max_score, score)

print(max_score)


