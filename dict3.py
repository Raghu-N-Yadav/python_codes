#creating empty dictionary
Dict = {}
Dict1 = {1:{5:'wow',7:'lol'},2:{9:'gh',11:'asd'}}
#adding elements to dictionary
Dict[1] = 'wrong'
Dict['name'] = 'raghu'
Dict[4] = 'super'

print(Dict)
print(Dict1)
#accessing using key
print(Dict['name'])
print(Dict[4])
print(Dict1[1][5])

#accessing using get
print(Dict.get('name'))
print(Dict.get(1))
#******
print(Dict1.get(2).get(9))