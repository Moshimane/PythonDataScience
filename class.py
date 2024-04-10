class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0
        
    def get_descriptive_name(self):
        return self.make + ' '+ self.model+ ' '+ self.year
    
    def read_odometer(self):
        return self.odometer_reading
    
    def update_odometer(self, mileage):
        self.odometer_reading += mileage
        

car = Car('Mercedes Benz', 'A200', '2024')

print(car.get_descriptive_name())

print(car.read_odometer())
print('Drive 133 km')

car.update_odometer(133)
print(car.read_odometer())


class Shape:
    def __init__(self, name):
        self.name = name
        self.area = None
        
    def get_name(self):
        return self.name
    
class Triagle(Shape):
    def __init__(self, base, height):
        super().__init__('Triagle')
        self.base = base
        self.height = height
        
    def area_calc(self):
        self.area = self.base * self.height / 2
    
class Square(Shape):
    def __init__(self, side):
        super().__init__('Square')
        self.side = side
        
    def area_calc(self):
        self.area = self.side * self.side
    
triagle = Triagle(3, 4)
square = Square(6)
print(triagle.get_name())
triagle.area_calc()
print(triagle.area)

class Father:
    def eyes(self):
        print('brown eyes')
        
    def skill(self):
        print('coding')

class Mother:
    def hair(self):
        print('blonde hair')
        
    def skill(self):
        print('cleaning')
        
class Child(Father, Mother):
    def personality(self):
        print('bubbly personality')
        
    def skill(self):
        Father.skill(self)
        Mother.skill(self)
        print('wrestling')
        
child = Child()
child.personality()
child.hair()
child.eyes()
child.skill()