#function with some given parameter

def myfun(x, y = 50):
    print("x: ", x)
    print('y: ', y)
    print('\n')

myfun(10)
myfun(9,11)

def add(x,y):
    z = x + y
    return z

q = add(2,3)
print(q)