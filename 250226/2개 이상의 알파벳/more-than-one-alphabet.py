A = input()

def sol(A):
    alpha_count = {}
    for i in range(len(A)):
        alpha_count[A[i]] = 1
        if len(alpha_count) >= 2:
            return True

    return False

if sol(A):
    print("Yes")
else:
    print("No")
