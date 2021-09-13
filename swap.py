##swaping two numbers
def swap(x,y):
    tem = x
    x = y
    y = tem
    return x, y
x, y = 2, 3
print(swap(x,y))
