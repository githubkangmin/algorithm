Spell = input().lower()

arr = [0]*26

for i in Spell:
    arr[ord(i)-ord('a')] += 1


maxV = max(arr)
cnt = 0
for i in arr :
    if(i == maxV) :
        cnt+=1

if cnt > 1 :
    print('?')
else:
    print(chr(arr.index(max(arr))+ord('a')).upper())

# print(chr(maxV).upper())

# print(chr(max(arr)))
