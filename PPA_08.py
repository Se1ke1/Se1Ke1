#팰린드롬수를 판단
from collections import deque
num=input()
arr_num=deque(list(num))
while arr_num:
    a=arr_num.popleft()
    b=arr_num.pop()
    if a==b:
        c=True
        continue
    else:
        c=False
        break
if c:
    print(f"{num}은 팰린드롬!")
else:
    print(f'{num}은 팰린드롬이 아님')