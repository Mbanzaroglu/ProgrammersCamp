
#calcutating the factorial of the given number
#%%
number = int(input("Please enter a number to calculate the factorial."))
temp = 1
for i in range(1,number+1):
    temp = temp * i
result = temp 
print("The factorial of the " + str(number) + " is " + str(result)) # "+" operation cannot be between int and string
#data types need to be same. Therefore convert integers to string format in order to display them with string.
#%%

#%%
#Addition of 2 matrices 

myMatrix = [[0 for x in range(3)] for y in range(3)]  #will ask for a data for 3*3 matrix
yourMatrix = [[0 for x in range(3)] for y in range(3)]#this is a special way to fulfill the matrices in python.
print(myMatrix)
sumMatrix = [[0 for x in range(3)] for y in range(3)]
def matrixDec(matrix):
    for x in range(0,3):
        for y in range(0,3):
            matrix[x][y] = int(input("Please enter a value for matrix : "))
def matrixAdd(matrixA, matrixB):
    for x in range(0,3):
        for y in range(0,3):
            sumMatrix[x][y] = matrixA[x][y] + matrixB[x][y]
            
    return sumMatrix
      
print("First Matrix")
matrixDec(myMatrix)
print("Second Matrix")
matrixDec(yourMatrix)

sumMatrix = matrixAdd(myMatrix, yourMatrix)
print(sumMatrix) 
#%% ANOTHER SOLUTION
myMatrix = []  #will ask for a data for 3*3 matrix
yourMatrix = []
sumMatrix = []
def matrixDec(matrix):
    for x in range(0,3):
        matrix.append([])#we appended 3 rows inside our matrices
        for y in range(0,3):
            matrix[x].append(int(input("Please enter a value for matrix : "))) #we inserted 3 elements to each row just has been created.
def matrixAdd(matrixA, matrixB):
    for x in range(0,3):
        sumMatrix.append([])
        for y in range(0,3):
            sumMatrix[x].append(matrixA[x][y] + matrixB[x][y])
            
    print(sumMatrix) 
      
print("First Matrix")
matrixDec(myMatrix)
print("Second Matrix")
matrixDec(yourMatrix)

matrixAdd(myMatrix, yourMatrix)
#%%