N= int(input())
for i in range(1,N+1):
    x= "*"*i
    print(F"{x:>{N}}")
# 문자열 포매팅에서 중괄호 {} 는 변수를 읽을 수 있게 해준다. 중괄호 없이  x:>N으로 쓰면 그냥 문자열로 읽음