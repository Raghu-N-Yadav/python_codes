#creating a class
class Dog:

    att1 = 'mammal'
    att2 = 'dog'

    def fun(self):
        print('i\'m a ', self.att1)
        print("i'm a ",self.att2)

rod = Dog()

print(rod.att1)
rod.fun()