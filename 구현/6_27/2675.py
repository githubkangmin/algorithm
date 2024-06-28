A = int(input())
B = int(input())
C = int(input())


gop = A*B*C

gop = list(map(int,str(gop)))


list = [0]*10

for i in gop:
    list[i] += 1


for i in list:
    print(i)