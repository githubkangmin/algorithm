#sol1)
n = int(input())

numbers = list(map(int,input()))

sum=0

for i in numbers:
    sum +=i

print(sum)

# #sol2)
# n = int(input())
#
# numbers = input()
#
# sum =0
#
# for i in numbers:
#     sum += ord(i) - ord('0')
#
# print(sum)