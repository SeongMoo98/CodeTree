# 길이가 N인 문자열 A
# 적잘하게 특정 횟수만큼 오른쪽으로 Shift하여 Run-Length Encoding을 진행했을때 길이가 최소가 되도록

# Run - Length Encoding
# 연속해서 나온 문자와 연속해서 나온 개수로 나타내는 방식

# ex) aaabbbbcaa
# a:3, b:4, c:1, a:2
# ==> a3b4c1a2, 길이 8

# 이 Run-Length Encoding 이후 결과중 최소 길이

A = list(map(str,  ' '.join(input()).split()))
N = len(A)

count = 0
min_len = 99
while True:
    if count > N:
        break

    # shift
    temp = A[-1]
    A[1:] = A[0:N-1]
    A[0] = temp

    run_len = [A[0], 1]
    same_idx = 0
    for i in range(1,N):
        if run_len[same_idx] == A[i]:
            run_len[same_idx+1] += 1
        else:
            run_len.append(A[i])
            run_len.append(1)
            same_idx += 2
    s = ""
    for i in range(len(run_len)):
        s += str(run_len[i])
    
    min_len = min(min_len, len(s))
    count += 1
print(min_len)


