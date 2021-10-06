#finding a contgous sub array 
myArray = []
x = int(input('Number of items'))
for i in range(x):
    myArray.append(int(input('Enter number'))) #apeending elements into the array

def find_subArray(array,start,end):
    length = len(array)
    if length = end +1:
        return array
    else :
        myArray = []
        for i in range(len(array)):
            


print(myArray)

#function to add all elements of an array
def add_up(array):
    k = 0
    for i in array:
        k += i
    return k

'''# Prints all subarrays in arr[0..n-1]
def printSubArrays(arr, start, end):
    newArray = []
     
    # Stop if we have reached the end of the array   
    if end == len(arr):
        return
     
    # Increment the end point and start from 0
    if start > end:
        #return 
        printSubArrays(arr, 0, end + 1)
         
    # Print the subarray and increment the starting
    # point
    else:
        newArray.append(arr[start:end + 1])
        #return 
        printSubArrays(arr, start + 1, end)   
    return newArray   '''       

'''
def subArray(arr, n):
    newArray = []
 
    # Pick starting point
    for i in range(0,n):
 
        # Pick ending point
        for j in range(i,n):
 
            # Print subarray between
            # current starting
            # and ending points
            for k in range(i,j+1):
                newArray.append(arr[k])
    return newArray
'''
#print(add_up(myArray))
#print(printSubArrays(myArray,0,0))
#print(myArray, length+1)