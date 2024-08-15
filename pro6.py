rollno=input("Enter your roll no:")

brachname=rollno[0:2]

print(brachname)

if brachname=='CS' or brachname=='Cs' or brachname=='cS' or brachname=='cs':
    print("\n{} is computer science student:".format(rollno))
else:
     print("\n{} is not computer science student:".format(rollno))