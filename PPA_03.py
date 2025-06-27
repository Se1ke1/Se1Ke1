for i in range(10):
    for j in range(1,11):
        if (i!=0 and i%3==0) or (j!=0 and j%3==0):
            num='박수짝'
            if (i!=0 and i%3==0) and (j!=0 and j%3==0):
                num=num+'짝'
            print(f'{10*i+j} : {num}',end="\t")
        else:
            print(f'{10*i+j} : {10*i+j}',end="\t")
    print()