N , M = map(int,input().split()) # 두 값 입력 받아서 하나씩 리스트에 저장
L = list(map(int,input().split()))
L.sort()
first = 0
second = 1
third =2
sum = L[first] + L[second] + L[third]
answer = sum
for i in range(first, N-2, 1) :
    for j in range(i+1, N-1, 1) :
        for k in range(j+1, N, 1) :
            sum = L[i]+L[j]+L[k]
            if(abs(M-sum)<abs(M-answer)) :
                answer = sum
print(answer)

# 오답체크
# 1. L= l.sort().reverse

# 2. L= l.sort()

#sort()메서드
#   리스트 객체에 종속된 멤버 메서드
#   리스트를 오름차순으로 정렬하고 None 값을 반환한다. 따라서 sort()를 쓸 때에는 등호로 다른 변수에 할당할 것이 아니라 그냥 리스트 클래스에 .으로 메서드 접근을 해야 한다.
#   내림차순으로 정렬하는 방법 sort(reverse=True)

#메서드 두개 연달아서 쓰는 방법
#