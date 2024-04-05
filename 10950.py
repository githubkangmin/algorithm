#a+b 근데 print 문의 개수 조절하는 것이 난이도가 높음.
# 제어문의 개수를 조정하는게 아니라 일일히 다 쓰는건가?
# 인풋값을 어떻게 받는거지
# 인풋값을 한번에 받는데 어떻게 하는거지


a= int(input())

for i in range(a):
    b, c = map(int, input().split())
    print(b+c)