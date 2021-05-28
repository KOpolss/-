class Car:
    def __init__(self,make, model, year_of_manufacture, speed = 0):
        self.make = make
        self.model = model
        self.year_of_manufacture = year_of_manufacture
        self.speed = speed

    def __increase_speeds__(self):
        self.speed += 5

    def __decrease_speeds__(self):
        self.speed -= 5

    def __stop__(self):
        self.speed = 0 

    def __speed_display__(self,speed):
        print(f'{speed} {self.speed}')

    def __reversal__(self):
        self.speed -= 5
        self.speed += 5

car = Car("audi","m5",2010)
car.__increase_speeds__()
car.__reversal__()
car.__speed_display__("speed")
print(car.model)