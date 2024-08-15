num=0
sum=0
num=input("Enter term:")

while(1):
 if(not num.isnumeric()):
    num=input("Enter only number value:")
 else:
    break
for i in range(int(num)+1):
    sum+=i
print("sumn of {} value is {}".format(num,sum))