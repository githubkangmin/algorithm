S=str(input())

arr=[0]*26

for i in S:
    arr[ord(i)-ord('a')]=arr[ord(i)-ord('a')]+1

for i in arr:
    print(i,end= " ")

#ord 메서드와 아스키코드

#ord()메서드에서 'i'가 아니라 i를 넣어야 하는 이유
# 'i'를 문자로 인식하게 됨 for문에서 쓰는 각자의 요소로 인식하도록 해야됨
