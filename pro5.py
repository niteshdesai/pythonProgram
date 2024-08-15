blood=('A-','A+','B-','B+','O-','O+','AB-','AB+')
p1=0
while(1):
  if(p1==0):
   person1=input("Enter Person1 Blood Group : ").upper()
   if(person1 in blood):  
       p1=1
  else:
     person2=input("Enter Person2 Blood Group : ").upper()
     if(person2  in blood):
       break
    

 
  
if(person1==person2):
   print(person1,"  and ",person2," blood group is match")
else:
   print(person1," and ",person2," blood group is not match")