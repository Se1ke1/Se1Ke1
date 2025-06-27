f_list=["Claire","Charlie","Martin","Elizabeth","Amy","Claudia","Tom","Bob"]
#sort와 Max 없이 가장 긴 텍스트를 찾아내는 법?
count=0
loc_x=0
for i in range(len(f_list)):
    count_tmp=len(f_list[i])
    if count_tmp>count:
        count=count_tmp
        loc_x=i
print(f_list[loc_x])
