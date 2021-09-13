#checking number is a strong or not
#ex :32 is strong if 3! +2! = 32

#function to calculate factorial
def fact (num):
    x = int(num)
    mul = 1
    for i in range(1,x+1):
        mul *=i
    return mul

num = input('enter a number:: ')
add = 0

#checking
for i in num:
    add += fact(i) 

if add == int(num):
    print('it is a strong numbert')
else:
    print('not a strong number')