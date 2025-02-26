n = int(input())

# Please write your code here.
def recursion(depth):

    if depth == n:
        return

    print("HelloWorld")
    recursion(depth+1)
    
recursion(0)
