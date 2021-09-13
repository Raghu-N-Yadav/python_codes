#deleting from a dictionary
Dict = { 5 : 'Welcome', 6 : 'To', 7 : 'Geeks',
        'A' : {1 : 'Geeks', 2 : 'For', 3 : 'Geeks'},
        'B' : {1 : 'Geeks', 2 : 'Life'}}

print(Dict)

#using del to delete an iteam

del Dict[6]
print(Dict)
del Dict['A'][2]
print(Dict)

Dict1 = {1:'happy',2:'lo',3:'sed'}
print(Dict1)

#using pop// pop is using key
pop_ele = Dict1.pop(1)
print(Dict1)
print(pop_ele)

#using popitem.. from from the last
Dict2 = {1:'school',2:'gone',3:'sum'}
print(Dict2)
pop_ele = Dict2.popitem()

print(Dict2)
print(pop_ele)