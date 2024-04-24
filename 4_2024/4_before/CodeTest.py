# #45분 빼는 코드
# a, b = map(int, input().split())
#
# if b>=45 :
#     print(str(a)+" "+str(b-45))
# else:
#     if a != 0:
#         print(str(a-1)+" "+str(b+15))
#     if a == 0:
#         print(str(23) + " " + str(b+15))

# 요리가 끝나는 시간 계산
#
# a, b = map(int, input().split())
# c= int(input())
#
# hour = int(c/60)
# min = c%60
#
# if  min+b<60 :
#     if a+ hour <24 :
#         print(str(a+hour)+" "+str(min+b))
#     else :
#         print(str(a+hour-24)+ " " + str(min+b))
# else:
#     if a+ hour <24 :
#         print(str(a+hour+1)+" "+str(60-(min+b)))
#     else :
#         print(str(a+hour+1-24)+ " " + str(60-min+b)))

a, b = map(int, input().split())
c= int(input())

d= int(c/60)
minV = c%60

if b+minV < 60 :
    if a+d>=24:
        print(a+d-24, b + minV)
    else :
        print(a+d,b+minV)
else:
    if a+d+1>=24:
        print(a+d+1-24,b+minV-60)
    else:
        print(a+d+1,b+minV-60)