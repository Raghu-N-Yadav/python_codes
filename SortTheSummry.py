def groupSort(arr):
    newDic = {}
    for i in sorted(arr):
        if i in newDic:
            newDic[i]+=1
        else:
            newDic[i] =1
    
    newArr2 = []
    # a = sorted(newDic.values())
    # a.reverse()
    # print(newDic)
    # print(a)
    # myArr1 = []
    # k =0
    # while(k < len(a)):
    #     for i in newDic:
            
    #         if newDic[i] == a[k]:
    #             myArr = []
    #             myArr.append(i)
    #             myArr.append(a[k])
    #             myArr1.append(myArr)
    #             break
    
    # print(myArr1)
    
    
    for obj in newDic:
        newArr1 = []
        newArr1.append(obj)
        newArr1.append(newDic[obj])
        newArr2.append(newArr1)
    return newArr2