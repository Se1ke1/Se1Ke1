num=int(input())
count=1
for i in range(num):
    list_a=list(range(count,count+num))
    count+=num
    print(*list_a)