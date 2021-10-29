def recu(n):
    sum = 0
    if(len(n) ==1):
        return n
    else:
        for i in n:
            sum += int(i) 
    return recu(str(sum))
def superDigit(n, k):
    n = n*k
    return recu(n)

print(superDigit('2322'))