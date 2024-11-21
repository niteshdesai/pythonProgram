
import sys
myfile=open(sys.argv[1],"r")

data=myfile.read()
print(data)

myfile.close()
rep=data.replace(sys.argv[2],sys.argv[3])

myfile=open(sys.argv[1],"w+")

myfile.write(rep)

myfile.seek(0)

print("\n")
print("Replaced file data")
print("\n")

print(myfile.read())

myfile.close()