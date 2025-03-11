n, k = map(int, input().split())
x = []
c = []

for _ in range(n):
    pos, char = input().split()
    x.append(int(pos))
    c.append(char)

# Please write your code here.
# N명이 위치 x에서 G, H를 받음
# G는 1, H는 2
# 사진의 크기가 K

# 위치는 1 ~ x
MAX_X = 10000
positions = [0] * (MAX_X + 1) 

for pos, ch in zip(x, c):
    positions[pos] = ch

max_score = 0
for i in range(1, MAX_X-k+1):
    score = 0
    temp = positions[i:i+k+1]
    score += temp.count("G")
    score += 2 * temp.count("H")
    
    max_score = max(max_score, score)

print(max_score)


