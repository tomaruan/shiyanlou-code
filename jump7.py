a=0
while a<100:
    a+=1
    if a%7==0 or (a-7)%10==0 or a-70<10 and a-70>0:
        continue
    print(a)
