#2번째 프로그램
while True:
    num=input('1~99 사이의 정수를 입력 :')
    if num=='0':
        print("프로그램을 종료합니다!")
        break
    if '3' in num or '6' in num or '9' in num:
        print('박수',end="")
        for c in num:
            if c in '369':
                print('짝',end="")
        print()