#using while loop
i = 1
mylist = []
mylist1 = []
while i<=20:
    if i %2 == 0:
        mylist.append(i)
        i=i+1
    else:
        mylist1.append(i)
        i+=1

j = 0
while j<10:
    print(mylist[j],end = '\t')
    print(mylist1[j],end = '\t')
    j+=1

print(mylist)
print(mylist1)