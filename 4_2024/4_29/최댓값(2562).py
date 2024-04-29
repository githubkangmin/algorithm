l = []
for i in range(9):
    numbers = int(input())
    l.append(numbers)
m=max(l)
print(m)
print(l.index(m)+1)

#오답
#for문 안에서 l = []로 선언을 하면 매 반복마다 리스트가 초기화돼서 리스트에 가장 마지막 값만 들어간다