A, B = input().split()

A= list(map(int,A))
B= list(map(int,B))

A.reverse()
B.reverse()

A=int(''.join(map(str,A)))
B=int(''.join(map(str,B)))


print(max(A,B))
