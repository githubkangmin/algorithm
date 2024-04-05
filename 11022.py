# A+B 과정까지 같이 출력하기
n = int(input())
p=1
for i in range(n):
    a, b = map(int, input().split())
    print(f"Case #{p}:", a,"+",b,"=",a+b)
    p+=1