#'a'==97, 'z'==122
cha=input("소문자 알파벳 하나를 입력하십시오 :")
t=ord(cha) - 96
for i in range(t):
    for j in range(t-i):
        print(chr(j+97),end="")
    print()