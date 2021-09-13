#checking either the number is is palladrom or not

x = input('enter a number ::')

rev = x[::-1]
if rev == x:
    print('it is a pallandrom')
else:
    print('not a pallandrom')