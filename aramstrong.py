#checking number is armstrong or not\
#eg = 407 is arm str coz 4 cube +0 cube +7 cube = 407

n = input('enter a number :: ')
a = int(n)
lenght = len(n)
mylist = []
for i in n:
    mylist.append(i)

sum = 0
for i in range(0,lenght):
    x = int(mylist.pop())
    sum =sum + x**3

if sum == a:
    print('it is armstrong')
else :
    print('not a arm strong')

print('sum of the digits is ::', sum)
#print(mylist)