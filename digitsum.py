#adding digits of a number
n = input('enter a number :: ')

lenght = len(n)
mylist = []
for i in n:
    mylist.append(i)

sum = 0
for i in range(0,lenght):
    x = int(mylist.pop())
    sum =sum + x

print('sum of the digits is ::', sum)
#print(mylist)
