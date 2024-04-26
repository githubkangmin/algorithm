#x보다 작은 수
N , X =map(int,input().split())
A = list(map(int,input().split()))

smaller = []

for i in A:
    if i < X :
        smaller.append(str(i))
    else:
        pass

result = ' '.join(smaller)
print(result)


#if문 아래에 smaller = i로 하면 sammller는 배열이 아니라 정수로 바뀌게 된다
# 리스트에 저장된 객체 메서드인 append를 써서 추가해야 한다.

#join 메서드는 문자열에서만 통하는 메서드이므로 str로 바꿔서 써줘야 한다.
#join 메서드는 모두 ㅁ