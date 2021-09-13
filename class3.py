#using claas again 

class Car:

    def __init__(self,model,color):
        self.model = model
        self.color = color

    def show(self):
        print('model of car is ', self.model)
        print('color of car is ', self.color)

audi = Car('A4', 'Black')
maruti = Car('vista',"white")

audi.show()
Car.show(maruti)