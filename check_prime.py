#checking either a number is prime or not
x = int(input('enter a number'))
rem = int(x / 6)
a = (6 * rem) + 1
print(a)
b = (6 * rem) - 1
print(b)
if x == a or x == b:
    print('it is prime')
    #break
else:
    print('it is not prime')
    #break

'''else:
    print('not a prime number')

for i in range(2,x+1):
    if x % i == 0:
        print('not a prime')
        break
print('it is a prime number')
        


print('it is prime')'''