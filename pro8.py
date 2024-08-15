students=input("How Many Students : ")
p=0
i=1

while(1):
 if(not students.isnumeric()):
    students=input("How Many Students : ")
 else:
    break
while(i<=int(students)):
    m=input("Enter {} Student Marks : ".format(i))
    if(not m.isnumeric()):
       m=input("Enter {} Student Marks : ".format(i))
    else:
      m=int(m)  
      if(m>100 or m<0):
        print("please,enter valid student marks")
        continue
      if(m>=40):
        p+=1
      i+=1    
print("Percantage of Passing Students {}%".format((p*100)/int(students)))