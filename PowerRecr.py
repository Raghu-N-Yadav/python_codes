'''
calculating x**n using recursion
'''
def pow(x,n):
    if n == 0:
        return 1
    elif n%2 == 0:
        y = pow(x,n/2)
        return (y*y)
    elif n%2 ==1:
        return x* pow(x,n-1)

print(pow(2,5))