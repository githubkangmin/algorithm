# 입력값의 줄 수에 따라서 출력값 줄 수가 달라지도록 코딩 + 0 0 이 마지막에 들어오고 이건 출력 안해야 됨
while(True):
    add1, add2 = input().split()
    if int(add1) == 0 and int(add2) == 0:
        break;
    print(int(add1) + int(add2))


# split을 하면 문자열을 숫자열로 받았어도 문자열로 저장함.
# if문을 먼저 써야 0 0 을 출력하지 않고 break문으로 들어간다.
# 입력값을 두개 받으려면 .split()을 두 변수로 따로 저장해야 한다. 다만 split을 쓰면 저장될 떼 공백을 기준으로 분리하여 리스트로 저장된다