import sys

n = int(sys.stdin.readline().rstrip())

for i in range(n):
    A, B = map(int, sys.stdin.readline().rstrip().split())
    print(A+B)

## 런타임 에러? 런타임 에러가 왜 나지? -> 탈출조건 안줌