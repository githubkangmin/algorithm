#최소, 최대
N = int(input())
numbers = list(map(int,input().split()))

maxVal = max(numbers)
minVal = min(numbers)

print(minVal, " ", maxVal)


# input() 함수 : python 내장함수로 입력받은 값들을 문자열로 저장하는 함수
# 문자열로 저장하는 것과 숫자열로 저장하는 것의 차이점. 숫자로써 동작해야 하는 코드에서 숫자로 인식을 안하게 돼서 문제가 생김 숫자로써 동작이 필요하다면 숫자열로 만들어 주어야 한다.

# .split() : Python에서 객체에 종속된 메서드

# max() min()


#print() 괄호 안에 ,와 +의 차이
#   안의 요소끼리 자료형이 같아야 하는 것은 + 달라도 되는 것은 , 또한 ,은 두 값을 띄어쓰기로 나눈다.
#

