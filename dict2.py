#adding and updating a dictionary,, only one value can be added at atime
Dict ={}

#adding
Dict[0] = 'Hi'
Dict[3] = 'lol'
Dict[2] = 5

print(Dict)

Dict2 = {1:'hello',3:{'a':'hi','b':'hoho'}}
#upading existing value
Dict[2] = 'Kuch'
#updating in nested dictionary
Dict2[3]['a'] = 'bye'

print(Dict)
print(Dict2)