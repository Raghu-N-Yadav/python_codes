#deleting items from a set using remove, discard,pop, clear
set1 = set([1,2,3,4,5,6,7,8])
set2 = set('i am what you are')
print(set1)
print(set2)

#using remove
#set1.remove(0)
#can not use index 0 to remove 
set1.remove(1)
#set2.remove(1)
print('used remove')
print(set1)
#print(set2)

#using discard
set1.discard(2)
#set2.discard(2)
print('used discard')
print(set1)
#print(set2)
#using pop
print('used pop')
set1.pop()
#only pop and clear is working on a string set
set2.pop()
print(set1)
print(set2)

#using clear to clear whole set
print('used clear')
set1.clear()
set2.clear()
print(set1)
print(set2)