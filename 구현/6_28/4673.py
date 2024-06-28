all = list(range(1,10001))

#생성자가 있는 숫자인지 판단 후 제거 생성자가 있는지 어떻게 알지? 이거로 하는거네
for i in range(1,10001):
    for j in str(i):
        i += int(j)
    try:
        all.remove(i)
    except ValueError:
        pass

for i in all:
    print(i)

#생성자가 없는 숫자 판단

#그냥 계속 생성해나가면서 지우기-어디까지 트리거로 잡아야 하지?
# def rself(n):
#     if n>10000:
#         return
#     if n<10:
#
#
#     return rself()
#
#
# while (n>10000):

