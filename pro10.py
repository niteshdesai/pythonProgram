no=input("Enter Any Number:")
while(1):
 if(not no.isnumeric()):
    no=input("Enter Any number: ")
 else:
    break
no=int(no)
print(no,end=" ")
while(no!=1):
    if(no%2==0):
        no=int(no/2)
        print(no,end=" ")
    else:
        no=(no*3)+1
        print(no,end=" ")