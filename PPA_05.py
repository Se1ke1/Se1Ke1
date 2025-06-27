#1:순서대로 늘어나는 도형 y=x
def job_1(num:int):
    for i in range(num):
        for j in range(i):
            print('*',end="")
        print('*')
#2:순서대로 감소하는 도형 y=-x+n
def job_2(num:int):
    for i in range(num):
        for j in range(num-i):
            print('*',end="")
        print()
#3:순서대로 감소하되 우측 정렬된 도형 y=-x+n
def job_3(num:int):
    for i in range(num):
        for j in range(i):
            print(end=" ")
        for j in range(num-i):
            print('*',end="")
        print()
#4:순서대로 증가하되 우측 정렬된 도형 y=x
def job_4(num:int):
    for i in range(num):
        for j in range(num-i-1):
            print(end=" ")
        for i in range(i):
            print("*",end="")
        print("*")
#5:순서대로 증가하되 양측으로 증가하는 도형 y=2x+1
def job_5(num:int):
    for i in range(num):
        for j in range(num-i-1):
            print(end=" ")
        for j in range(i):
            print("**",end="")
        print("*")
#6:순서대로 감소하되 양측으로 감소하는 도형 y=-2x+2n+1
def job_6(num:int):
    for i in range(num):
        for j in range(i):
            print(end=" ")
        for j in range(num-i-1):
            print("**",end="")
        print("*")
#7:상하가 접합된 5/6번 도형
#8:꼭짓점이 접합된 5.6번 도형
while True:
    cmd=int(input("출력 도형의 모양 번호를 입력하세요(종료 시 0 입력) :"))
    if cmd==0:
        print("삼각형 그리기 프로그램을 종료합니다.")
        break
    num_n=int(input("출력 도형의 라인 수를 홀수(3~15)로 입력하세요 :"))
    if num_n%2==0:
        print("Input Error")
    elif cmd==1:
        job_1(num_n)
    elif cmd==2:
        job_2(num_n)
    elif cmd==3:
        job_3(num_n)
    elif cmd==4:
        job_4(num_n)
    elif cmd==5:
        job_5(num_n)
    elif cmd==6:
        job_6(num_n)
    elif cmd==7:
        job_5(num_n)
        job_6(num_n)
    elif cmd==8:
        job_6(num_n)
        job_5(num_n)
    else:
        print('Input Error')