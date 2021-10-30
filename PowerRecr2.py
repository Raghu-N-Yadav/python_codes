'''
calculating x**n module m
'''
def pow(x,n,m):
    if n == 0:
        return 1
    elif n%2 ==0:
        y = pow(x,n/2,m)
        return (y*y)%m
    elif n%2 ==1:
        return (x%m)* pow(x,n-1,m)

print(pow(1000,1000,3))