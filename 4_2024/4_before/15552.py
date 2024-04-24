#"Case #x: "를 A+B와 함께 출력

count= int(input())
sum=0
n=1
for i in range(count):
    a, b = map(int,input().split())
    sum= a+b
    print(f"Case #{n}:", sum)
    n+=1