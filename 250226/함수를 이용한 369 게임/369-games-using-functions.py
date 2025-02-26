A, B = map(int, input().split())

def sol(A, B):
    count = 0
    for num in range(A, B+1):
        if num % 3 == 0:
            count += 1
            continue

        for s in str(num):
            if s in ['3','6','9']:
                count += 1
                break

print(sol(A, B))
