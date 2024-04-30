N, M = map(int, input().split())

l= []

l = [0] * N

for _ in range(M):
    i, j, k = map(int, input().split())
    l[i-1:j] = [k] * (j - i + 1)

# l.reverse()

for num in l:
    print(num, end=' ')


# map함수의 결과값을 할당시킬 때에는 항상 대상이 "반복가능한 객체"여야 한다.
#    l[i:j+1] = k로 쓰면 map의 결과값을 하나의 단일값에 할당하는 것이 되므로 그 값이 제대로 보전되지 않는다.

# 하나의 값이 들어간 리스트를 반드는 방법
#   1.반복문으로 만들기
#         for i in range(N):
#             l.append(0)
#   2. 리스트에 값 곱하기
#       l = [0] * N  # N개의 요소를 0으로 초기화한 리스트 생성