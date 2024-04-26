while(True):
    a, b = input().split()
    a = int(a)
    b = int(b)
    print(a + b)

while True:
    try:
        A, B = map(int, input().split())
        print(A+B)
    except:
        break