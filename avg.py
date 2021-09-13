#calculating average of numbers in tne list
n = int(input('enter number of elements you want in the list'))
my_list = []

for i in range(0,n):
    num = int(input('enter the number'))
    my_list.append(num)

add = 0
for i in my_list:
    add +=i

avg = add/n
print("average of the numbers is ", round(avg,2))
