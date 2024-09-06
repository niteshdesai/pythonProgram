def createMat(x,y,mname):
    for i in range(0,x):
      mname.append([])
    for i in range(0,x):
      for j in range(0,y):
        mname[i].append(j)
    return mname
def MatValue(x,y,mat):
   for i in range(x):
     for j in range(y):
        print("Enter for matrix value in row",i+1,"and col",j+1)
        mat[i][j]=int(input())
   return mat
def display(x,y,mat):
   for i in range(len(mat)):
    for j in range(len(mat)):
        print(mat[i][j],end=" ")
    print()

# mat=[]
# mat2=[]
# mat=createMat(2,2,mat)
# mat2=createMat(2,2,mat2)
# print("Enetr value for matrix 1:")
# mat=MatValue(2,2,mat)
# print("Enetr value for matrix 2:")
# mat2=MatValue(2,2,mat2)
# print(mat)
# print(mat2)



       