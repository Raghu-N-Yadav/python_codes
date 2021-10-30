def smallestNegativeBalance(debts):
    balance = {}
    for i in debts:
        if i[0] in balance:
            balance[i[0]] -= int(i[2])
        else:
            balance[i[0]] = -int(i[2])
        if i[1] in balance:
            balance[i[1]] += int(i[2])
        else:
            balance[i[1]] = int(i[2])
            
    #print(balance)
    #print(debts)
    minBal = min(balance.values())
    arr = []
    for i in balance:
        if balance[i] < 0:
            if balance[i] == minBal:
                arr.append(i) 
    #print(sorted(arr))
    s = ['Nobody has a negative balance']
    if(arr):
        return sorted(arr)
    else:
        return s


arr =[['alex','black',5],['black', 'alex',3], ['casey','alex',7]]
print(smallestNegativeBalance(arr))