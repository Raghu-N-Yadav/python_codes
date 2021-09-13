##find greatest number in the list



n = int(input('nzumber of elements ::'))
mylist1 = []
for i in range(0,n):
    mylist1.append(int(input("element ::")))
    #print(mylist1[i])

'''def greatest_number(mylist, n):

    
    
    for i in range(0,n):
        mylist.append(int(input('Enter number:: ')))
        
    num = 0
    #first = mylist[0]
    for i in range(0,n):
        if mylist[i] > num: #first:
            num == mylist[i]
            print(num)
        else:
            continue
        return num

print(greatest_number(mylist, n))'''
#finding greatest number
#mylist = [1,2,3,4,5]
var = mylist1[0]
for i in range(0,len(mylist1)):

    if mylist1[i] >= var:

        var = mylist1[i]
        #print(var)

#not getting second largest from the code
k = var
j = 0
for i in range(0,len(mylist1)):
    if mylist1[i] == k:
        continue
    else:
        mylist1[i] >= j
        k = mylist1[i]

print('largest number in the last is ',var)
print('second largest number is ::', k)

#did same thing in these two lines 
use_list =sorted(mylist1)
print('Largest number is :',use_list.pop())
print('second largest number is ::', use_list.pop())