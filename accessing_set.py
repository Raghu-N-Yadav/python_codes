#accessing elements from a set
set1 = set('Raghunandan')
set2 = set([1,2,3,4,5])
#set3 = set(1,2,3,4) can not creat like this 

#can not access elemnts by index value need to use the loop
print(set1,'\n',set2)

#adding items using add and upadte

set1.add('yadav')
set2.update([9,11])

print(set1,'\n',set2)

for i in set1:
    print(i, end = '\t')
print('\n')

for j in set2:
    print (j, end = '\t')