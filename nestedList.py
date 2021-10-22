if __name__ == '__main__':
    arr = []
    arr2  = []
    arr3 = []
    #newL = []

    for _ in range(int(input())):
        name = input()
        score = float(input())
        arr = [name,score]
        arr2.append(arr)
        arr3.append(score)
    newL = list(set(arr3)) #removing duplicates
    newL.sort()
    x  = newL[1]
    y  = []
    for val in arr2:
        if val[1] == x:
          y.append(val[0])  
    y.sort()
    for i in y:
        print(i)
    #print (arr2,x,y)
    