#1번 프로그램
num_d=int(input('2자리 정수 입력 :'))
if num_d>=100 or num_d<10:
    print("Input Error")
elif num_d//10==num_d%10:
    print("YES! 10의 자릿수와 1의 자릿수가 동일합니다.")
else:
    print('NO! 10의 자릿수와 1의 자릿수가 동일하지 않습니다.')