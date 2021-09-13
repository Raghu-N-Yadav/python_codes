#doing dome math by using class

class Math:

    def __init__(self, f, s):
        self.f = f
        self.s = s

    def addition(self):
        print(self.f + self.s)

    def mul(self):
        print(self.f * self.s)

print('enter two numbers to do math')
x = int(input('first :'))
y = int(input('sec :'))
obj = Math(x,y)

obj.addition()
obj.mul()