#입력된 수만큼 문자열 띄어쓰기로 출력하기

num= int(input())

count = int(num/4)

for i in range(count):
    print("long", end=" ")
print("int", end= " ")