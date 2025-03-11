# N개의 수로 이루어진 수열 A
# M개의 수로 이루어진 수열 B

# 수열 B의 각 원소의 순서를 바꿔 나오는 수열을 "아름다운 수열"
# 수열 A에서 길이가 M인 연속 부분 수열 중 아름다운 수열의 수를 세기

N, M = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

count = 0
for i in range(len(A) - len(B) + 1):
    for j in range(i, i+len(B)):
        if A[j] not in B:
            break
    else:
        count += 1

print(count)