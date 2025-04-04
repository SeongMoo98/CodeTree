# N x N 크기의 Matrix에서 금을 최대한 많이 채굴
# 마름모 모양으로 단 한 번만 채굴 가능
# 마름모 모양을 지키는 한 이차원 영역을 벗어난 채굴도 가능하지만 Matrix 밖에는 금 x

# 마름모 모양이란 특정 중심점을 기준으로 K번 이내로 상하좌우에 인접한 곳으로 이동하는 것을
# 반복했을 때 갈 수 있는 모든 영역

# K = 0 일때는 특정 지점 1곳만

# 채굴에 드는 비용 : K^2 + (K+1)^2
# 금 한 개의 가격이 M일때, 손해를 보지 않으면서 채굴할 수 있는 가장 많은 금의 개수를 구하여라

N, M = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(N)]


## ***************** 시간 초과 ***************** ##
# # 마름모 크기 K
# # ==> 비용은 K^2 + (K+1)^2, 이익은 K * M
# d = [(-1, 0), (1, 0), (0, -1), (0, 1)]

# from collections import deque
# def make_diamond(i, j, K):
#     diamond = [(i, j)]
#     q = deque()  
#     visited = [[False] * N for _ in range(N)]

#     q.append((i, j))
#     visited[i][j] = True

#     for k in range(K):
#         temp = []
#         for dia_i, dia_j in diamond:
#             temp.append((dia_i, dia_j)) 
#         q = deque(temp)

#         while q:
#             ci, cj = q.popleft()

#             for di, dj in d:
#                 ni, nj = ci + di, cj + dj
#                 if 0 <= ni < N and 0 <= nj < N and visited[ni][nj] == False:
#                     visited[ni][nj] = True
#                     diamond.append((ni, nj))
#     return diamond

# res = 0

# for K in range(2*(N-1), -1, -1):
#     for i in range(N):
#         for j in range(N):
#             glod_count = 0
#             diamond = make_diamond(i, j, K)
#             for ci, cj in diamond:
#                 if matrix[ci][cj] == 1:
#                     glod_count += 1
            
#             if M * glod_count >= K**2 + (K+1)**2:
#                 res = max(res, glod_count)
# print(res)


# 해설)
# 마름모의 정의 : 중심점을 기준으로 K번 이내로 인접한 곳 까지 이동하는걸 반복했을 때 갈 수 있는 영역
#   ==> 중심점 위치 와 특정 위치 간의 맨해튼 거리 <= K

def get_gold_count(ci, cj, k):
    gold_count = 0
    for i in range(N):
        for j in range(N):
            if abs(i - ci) + abs(j - cj) <= k:
                gold_count += 1
    return gold_count

res = 0

for i in range(N):
    for j in range(N):
        for k in range(2*(N-1) + 1):
            gold_count = get_gold_count(i, j, k)

            if M * gold_count >= k**2 + (k+1)**2:
                res = max(res, gold_count)

print(res)
