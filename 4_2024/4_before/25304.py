#영수증 다시 계산해보는 프로그램
totals= int(input())
counts=int(input())

sum=0

for i in range(counts):
    price, quantity = map(int, input().split())
    sum += price*quantity

if sum == totals:
    print("Yes")
else:
    print("No")