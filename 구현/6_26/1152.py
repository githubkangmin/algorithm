st = input()

result = 0
check = False
for i in st:
    if  (('a' <= i)  and  (i <='z') or ('A'<=i) and (i<= 'Z')) :
        if check == False :
            result += 1
            check = True
    if i == ' ' :
        check =False

print(result)



# st = input().split()
#
# print(len(st))