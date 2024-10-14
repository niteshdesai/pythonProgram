import re
myfile = open("record.txt")
readdata = myfile.read()
pattern ="credit hours- (\\d+)\npoint - (\\d+.\\d+)"
data= re.findall(pattern,readdata)
print(data)
totalp=0
totalc = 0
for i in data:
    totalp +=(int(i[0])*float(i[1]))
    totalc += int(i[0])
print("CGPA : ",end=" ")
print(totalp/totalc)
myfile.close()