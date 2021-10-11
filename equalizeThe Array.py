def equalizeArray(arr):
    arr.sort()
    delete = 0
    count = 1
    i = 0
    value = 0
    while i < len(arr)-1:
        if arr[i] == arr[i+1]:
            count +=1
            #Value = count
        else:
            count = 1
            #delete = i
        if count > value:
            value = count
        i+=1
    return len(arr)- value

arr = [1,1,1,1,2,3,3,3,4,4]
print(equalizeArray(arr))