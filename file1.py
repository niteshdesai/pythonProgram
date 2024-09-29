import sys
myfile=open(sys.argv[1],"r")

data=myfile.read()
print(data)
rep=data.replace(sys.argv[2],sys.argv[3])

print("Replaced file data")

print(rep)

myfile.close()