#구구단(n단을 입력받은 뒤 구구단 n단을 출력하는 프로그램) 구구단 전체를 뽑는건 아님.
i = int(input())
for j in range(1,10):
    print(i,"*",j,"=",i*j)