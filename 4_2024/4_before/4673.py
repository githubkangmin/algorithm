# list = []
# start = 1
# for i in range(1,10001,1):
i = int(9876)
sum = int(i)
while(i > 0) :
    sum+=int(i%10)
    print(i%10)
    i= int(i/10)
print("총 합: " , sum)