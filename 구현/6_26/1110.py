init = num = input()
cycle = 0

if int(num) < 10 :
    init = num = '0'+num

while True:
    num = num[1]+ str((int(num[0])+int(num[1]))%10)
    cycle += 1
    if init == num:
        break
print(cycle)
