term=int(input("Enter No of Term : "))
sum=0
i=1
no=1

while(i<=term):
    sum=0
    for j in range(1,no):
        if(no%j==0):
            sum=sum+j
            
    if(no==sum):
        print(no)
        i+=1
    no+=1
