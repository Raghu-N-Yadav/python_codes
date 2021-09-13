#accessing elements of a list 
list = [1,2,3,4,5,6,7,'Yadav']
print('\n',list)
print(list[0],list[0:3],list[-1], list[-3:-1])

#deleting elements of a list using pop and remove ,, indext 0 does not work in removing
list.remove(1)
list.remove(4)
print(list)
list.pop()
#it will pop element from the last
print(list)