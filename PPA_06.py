#원점이 0,0이고 반지름이 5인 원 A에 대하여, X,Y좌표를 입력받아 원 내부에 있으면 True, 아니면 False를 출력
x,y=map(int,input().split())
if x**2+y**2>25:
    print(f'좌표({x},{y})는 원 바깥에 있음')
elif x**2+y**2==25:
    print(f'좌표({x},{y})는 원 위에 있음')
else:
    print(f'좌표({x},{y})는 원 안에 있음')