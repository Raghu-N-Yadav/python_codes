def recu(n):
    sum = 0
    if(len(n) ==1):
        return n
    else:
        for i in n:
            sum += int(i) 
    return recu(str(sum))
def superDigit(n, k):
    n = int(n)
    Sum = 0
    while(n >0):
        m = n%10
        Sum +=m
        n =n//10
    add = str(Sum)*k
        #n = n*k
    return recu(add)

print(superDigit('2322'))