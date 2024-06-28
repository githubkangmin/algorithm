S= input()

arr=[-1]*26



for i in S:
    arr[ord(i)-ord('a')]=S.index(i)

for i in arr:
    print(i,end = " ")
