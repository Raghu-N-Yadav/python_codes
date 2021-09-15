#adding two matrix 
raw1 = int(input('Enter number of rows in first matrix'))
col1 = int(input('Enter number of columns in first matrix'))
matrixRow1 = []

for i in range(raw1):
    matrixCol1 = [] #creating first column
    for j in range(col1):
        matrixCol1.append(int(input('enter number'))) #adding elements to column
        
    matrixRow1.append(matrixCol1) #creating first row
print('first Matrix is ', matrixRow1)

raw2 = int(input('Enter number of rows in second matrix'))
col2 = int(input('Enter number of columns in second matrix'))
matrixRow2 = []
for i in range(raw2):
    matrixCol2 =[]
    for j in range(col2):
        matrixCol2.append(int(input('enter a number')))
    matrixRow2.append(matrixCol2)
print(matrixRow2)

def addMatrix (matrix1,matrix2, raw1, col1):
    outputMatrix = []

    '''outputMatrix.append([])
    outputMatrix.append([])
    for i in range(len(matrix1)):
        outpuMatrixcol = []
        for j in range(len(matrix1[0])):
            outpuMatrixcol.append(int(matrix1[i]) + int(matrix2[j]))
        outputMatrix.append(outpuMatrixcol)
        print(outputMatrix)'''
        
    outputMatrix = [[0 for x in range(col1)] for x in range(raw1)] #creating 2d list
    for i in range(len(matrix1)):
        for j in range(len(matrix1[0])):
            outputMatrix[i][j] = matrix1[i][j] + matrix2[i][j] 
    return outputMatrix
print('Addition of both matrix : \n')
print(addMatrix(matrixRow1,matrixRow2, raw1, col1))
