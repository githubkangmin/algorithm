n = int(input())

result = 1

for i in range(1,n+1):
    result *= i

print(result)

def fac(n):
    if n == 0 or n == 1:
        return 1
    return n*fac(n-1)

print(fac(10))