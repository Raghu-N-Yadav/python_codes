#using functuons to do thinfs 
def user():
    print('you have done this using a function')

def sum():
    a = 0
    for i in range(1,11):
        a+=i
    return a

#calling function
user()
x = sum()
print(x)