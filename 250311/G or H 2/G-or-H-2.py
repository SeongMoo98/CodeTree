# N명이 일직선상에서 자신의 위치에 서있다
# 'G', 'H'가 정확히 같은 개수만큼 나오게 사진을 찍고 싶을 때
# 최대 사진의 크기를 구하라

# 사진의 크기 : 양쪽 끝에 있는 사람 간의 거리
# 사람이 1명 뿐인 경우 사진의 크기는 0


N = int(input())

pos, ch = [], []
for _ in range(N):
    x, c = input().split()
    pos.append(int(x))
    ch.append(c)

MAX_POS = max(pos)
positions = [0] * (MAX_POS + 1)

for i in range(N):
    positions[pos[i]] = ch[i]

def find_ans():
    for sub_len in range(len(positions), 0, -1):
        for i in range(len(positions) - sub_len + 1):
            sub_pos = positions[i:i+sub_len]
            if sub_pos[0] != 0 and sub_pos[-1] != 0:
                count_G, count_H = sub_pos.count("G"), sub_pos.count("H")
                if (count_G == count_H) or \
                    (count_G != 0 and count_H == 0) or \
                    (count_G == 0 and count_H != 0):
                    return sub_len - 1

print(find_ans())

