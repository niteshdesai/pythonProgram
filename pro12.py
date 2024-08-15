# Initialize an empty dictionary to store birthdays
birthdays={"nitesh":'13/03/2004',"jignesh":'30/03/2003',"Ashwin":'10/01/2003',"manish":'17/11/2004',"praveen":'19/04/2002'}



def find_birthdays(month):
    check=True 
    for name, date in birthdays.items():
        date_month = date.split('/')[1]
        
        if(date_month==month):
            print(name,"",date)
            check=False
    if(check):
     print("No One Birthday In This Month")     
        


month=input("Enter month:")

# chek=False
# if(not chek):
#    print("True")
# else:
#    print("False")
while(1):
   if(not month.isnumeric):
     month=input("Enter only digit month:")
   elif(int(month)>12 or int(month)<1):
    month=input("Enter month from 1 to 12:") 
   elif(len(month)==1):
     month="0"+month
     break 
   else:
      break  
find_birthdays(month)


          
 


