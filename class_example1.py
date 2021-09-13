#using init method 

class Person:

    def __init__(self, name):
        self.name = name 

    def say_hi(self):
        print('my name is ', self.name)

p = Person('Raghu')
p.say_hi()