#creating list 
list1 = []
print(list1)
list2 = ['raghu','n','yadav']
print(list2)
#multi dimensional list
list1 =['raghu', 'N',['yadav']]
print(list1)


#adding elements to the list using appened , insert and extend
list3 = []
list3.append(1)
list3.append(2)
print(list3)
#insert uses position to insert any elements
list3.insert(3, 'Yadav')
list3.insert(0,'number')
list3.insert(2, 'happy')
print(list3)

list3.extend([8,'two', 'somethoing'])
print(list3)