n = int(input())
res = "Yes" if n % 2 == 0 and ((n // 10) + (n % 10)) % 5 == 0 else "No" 
print(res)