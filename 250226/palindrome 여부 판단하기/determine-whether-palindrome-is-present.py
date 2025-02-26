A = input()

# Please write your code here.
def sol(A):
    if A == A[::-1]:
        return True

    return False

if sol(A):
    print("Yes")
else:
    print("No")