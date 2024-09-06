x=int(input("Enter Row :"))
y=int(input("Enter Col:"))
mat=[]
mat2=[]
for i in range(0,x):
    mat.append([])
    mat2.append([])
for i in range(0,x):
    for j in range(0,y):
        mat[i].append(j)
        mat2[i].append(j)

for i in range(x):
    for j in range(y):
        print("Enter for matrix value in row",i+1,"and col",j+1)
        mat[i][j]=int(input())
print("Enter Second Matrix value")
for i in range(x):
    for j in range(y):
        print("Enter for matrix 2 value in row",i+1,"and col",j+1)
        mat2[i][j]=int(input())  
 
result=[]
for i in range(0,x):
    result.append([])
 
for i in range(0,x):
    for j in range(0,y):
        result[i].append(j)
       

for i in range(x):
    for j in range(x):
      result[i][j]=mat[i][j]+mat2[i][j]

for i in range(len(result)):
    for j in range(len(result)):
        print(result[i][j],end=" ")
    print()




  







