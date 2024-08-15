num=input("Enter number:")
while(1):
 if(not num.isnumeric()):
    num=input("Enter numberrg: ")
 else:
    break
count=0
num=int(num)
for i in range(2,num):
    if(num%i==0):
        count=1
if(count==1):
    print("number is not prime")
else:
    print("number is prime")