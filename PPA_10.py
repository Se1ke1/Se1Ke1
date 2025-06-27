string_unpacked=input()
pre_cha=string_unpacked[0]
count=1
string_packed=''
for i in range(1,len(string_unpacked)):
    if string_unpacked[i]==pre_cha:
        count+=1
    else:
        string_packed=string_packed+f'{pre_cha}{count}'
        pre_cha=string_unpacked[i]
        count=1
string_packed=string_packed+f'{pre_cha}{count}'
print(string_packed,(len(string_unpacked)-len(string_packed)))