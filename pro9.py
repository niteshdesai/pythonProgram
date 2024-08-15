pre=1
nex=0
sum=0

num=input("Enter term:")
while(1):
 if(not num.isnumeric()):
    num=input("Enter term:")
 else:
    break
num=int(num)
for i in range(num):
    print(sum)
    sum=pre+nex
    pre=nex
    nex=sum