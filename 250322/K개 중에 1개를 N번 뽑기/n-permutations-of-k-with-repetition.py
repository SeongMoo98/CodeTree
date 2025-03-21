# 1 이상 K 이하의 숫자를 하나 고르는 행위를 N번 반복하여 나올 수 있는 모든 서로 다른 순서쌍 구하기

K, N = map(int, input().split())

arr = [i for i in range(1, K+1)]

def back(arr, res):
    if len(res) == N:
        [print(num, end=' ') for num in res]
        print()
        return

    for i in range(1, K+1):
        res.append(i)
        back(arr, res)
        res.pop()


back(arr, [])