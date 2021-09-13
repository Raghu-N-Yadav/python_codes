#checking number is perfect or not
# 6 is perfect coz its divisor 1 +2+3 = number itself i.e 6
num = int(input('Enter a number ::'))
add = 0
for i in range(1,num):
    if num % i == 0:
        add += i
    else:
        continue

if add == num:
    print('it is perfect number')
else:
    print('not a perfect number')