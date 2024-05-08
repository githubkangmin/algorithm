l = list(range(1,31))

for _ in range(1,29):
    number = int(input())
    if number in l:
        l.remove(number)

for i in l:
    print(i)

#입력값의 개수 제한을 줘서 난이도 조절했구나

#pop()과 remove()의 차이
#pop()은 인덱스를 지정해서 제거하는 것이고 remove()는 값을 비교해서 제거하는 것임.