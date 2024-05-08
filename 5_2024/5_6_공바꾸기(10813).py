N , M = map(int, input().split())

l=list()
for i in range(N):
    l.append(i+1)
temp=0

for i in range(M):
    j , k =map(int,input().split())
    temp=l[j-1]
    l[j-1]=l[k-1]
    l[k-1]=temp

for i in l:
    print(i,end=" ")

##리스트 생성하는 방법
##  l = list(range(1, N + 1)) list() 안에 range쓰면 원하는대로 생성가능


##변수 바꾸는 방법
##  자바에서배운대로 변환했는데 파이썬에서는 간단한 방법으로 가능함
##  l[j - 1], l[k - 1] = l[k - 1], l[j - 1]

##(숙련완료) 리스트로 된 숫자열 숫자열로만 출력하는 방법

##for문 요소없이 돌리는 방법
#   for _ in range(M):


##개선된 코드
# N, M = map(int, input().split())  # N과 M 입력 받기
#
# l = list(range(1, N + 1))  # 1부터 N까지의 리스트 생성
#
# for _ in range(M):
#     j, k = map(int, input().split())  # 스왑할 인덱스 입력 받기
#     l[j - 1], l[k - 1] = l[k - 1], l[j - 1]  # 두 요소의 위치를 스왑
#
# for i in l:
#     print(i, end=" ")  # 수정된 리스트 출력


