a=int(input())
b=list(map(int,input().split()))
c=int(input())
print(b.count(c))

#1. 내장함수와 특정 객체 타입의 메서드의 차이
#   객체타입의 메서드는 특정 데이터 타입의 클래스에 저장되어 있으므로 해당 데이터 타입의 메서드에 접근하기 위해서는 .을 이용해야 한다. ex)(str)은 .lower(), .upper(), .split()
#   내장함수(내장 메서드)는 특정 클래스에 저장된 것이 아니기 때문에 .으로 접근할 필요 없이 그냥 쓸 수 있다. ex) len(), print(), type()
#   -> print(count(c))는 아예 안되는 코드이다.


#2. 객체: 데이터(속성)와 그 데이터에 관련된 동작(메서드)를 하나로 묶은 것 실생활에서 우리가 인식할 수 있는 사물 또는 개념을 소프트웨어 내에서 모델링한 것임 ex) int는 객체 5는 인스턴스

#3. 이터러블 객체: 객체의 특성 중 하나라고 볼 수 있다. __iter__()->__next__()->StopIteration(예외 발생)
#   '__iter__()'메서드를 구현하는 모든 객체 이 메서드는 해당 객체를 순회할 수 있는 이터레이터를 반환.
#   이터레이터: 이터러블 객체로부터 생성되며, '__next__()'메서드를 통해 연속적인 요소를 하나씩 반환,이터레이터는 'next' 값에 접근할 때마다 하나의 요소를 제공하고, 모든 요소가 소진되면 StopIteration 예외를 발생시켜 순회의 끝을 알립니다.

#4. str()함수와 list()함수의 객체 처리방식 차이
#   str() 함수를 이용하여 어떤 객체를 문자열로 변환할 때, 파이썬은 해당 객체의 '__str__()'메서드를 호출 이 메서드가 적합하지 않다면 '__repr__()'메서드의 결과 사용함
#   '__str__()'메서드는 객체의 타입 정보와 메모리 주소를 나타내는 문자열을 반환
#   list()함수는 이터러블을 받아 그 요소들로 구성된 리스트를 생성함. map 객체도 이터러블이기에 map 객체에 저장된 요소를 하나씩 꺼내어 새로운 리스트의 요소로 추가


#5. map 함수
#   map함수는 결과값을 바로 저장하지 않고, 지연계산 방식을 사용. 바로 연산하지 않고 결과가 필요할 때 연산을 수행하는 것.
#   파이썬 내장함수이지만 반환하는 결과는 map 클래스의 인스턴스(이터러블)다. 그래서 map함수의 결과를 출력하면 메모리 주소가 나온다.
#   b=str(map(int,input().split())이 안되는 이유가 4. str()과 list 객체 처리 방식의 차이임.
#
#   a=int(input())
#   b=map(str,input().split())
#   c=int(input())
#   print(b.count(c))
#   -> 이 코드가 안되는 이유는 map 함수가 뱉은 이터러블 인스턴스가 count()메서드를 지원하지 않아서이다.

#-----------
#list에도 count()함수가 있음.
#for문으로 돌려도 될텐데 그냥 count 씀.
# cnt = int(input())
# nums = list(map(int, input().split()))
# target = int(input())

# num = 0
#
# for i in nums:
#     if i == target:
#         num += 1
#     else:
#         pass

# print(num)


#----------------------------오답 체크---------------------
# a=int(input())
# b=str(list(map(str,input().split())))
# c=str(int(input()))
# print(b.count(c))

## b=str(list(map(str,input().split())))
# 이 코드가 어떤 숫자들을 입력받고 리스트로 만들어서 그 리스트를 통으로 문자열로 만든 것이다. ["apple", "banana", "apple"] 와 "['apple', 'banana', 'apple']"의 차이인것.
#=>str(list())는 쓰지말자 list 통으로 문자열로 만드는 거임.
