#swaping first and last number of a given list
n = int(input("Number of elements ::"))
mylist = []
for i in range(0,n):
    mylist.append(input('enter number :'))
print(mylist)
last = len(mylist) - 1

temp = mylist[0]
mylist[0] = mylist[last]
mylist[last] = temp


print('afetr swaping first and last number list is ', mylist)