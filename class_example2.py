#another class ex 

class Dog:

    animal = 'Dog'

    def __init__(self, breed, color):
        self.breed = breed
        self.color = color

#ojects of the class
german = Dog('german', 'black')
buzo = Dog('desi','brown')

print('details of dofg 1')
print('german is a ',german.animal)
print('his breed is ', german.breed)
print('his color is ', german.color)

print('details of dog 2')
print('Buzo is a ',buzo.animal)
print('his breed is ',buzo.breed)
print('his color is ',buzo.color)

print('variable of class is ',Dog.animal)