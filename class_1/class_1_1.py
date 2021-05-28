class Dog:
    def __init__(self,name,weight,height,tail,ears,eyes):
        self.name = name
        self.weight = weight
        self.height = height
        self.__tail = tail  
        self.__ears = ears
        self.__eyes = eyes  
        
dog1 = Dog("raf",50,70,1,2,2)
print(dog1.name)

class Cat:
    def __init__(self,name,weight,height,tail,ears,eyes):
        self.name = name
        self.weight = weight
        self.height = height
        self.__tail = tail  
        self.__ears = ears
        self.__eyes = eyes 

cat1 = Cat("зефир",2,25,1,2,2)
print(cat1.name)

class Human:
    def __init__(self,name,surname,weight,hands,legs,fingers):
        self.name = name
        self.surname = surname
        self.weight = weight
        self.__hands = hands
        self.__legs = legs
        self.__fingers = fingers
    def say(self,walk):
        print(f'{walk}{self.name}')

human1 = Human("Валера","Соколов",40,2,2,20)
human2 = Human("Игорь","Дрокин",40,2,2,20)
human2.weight = 50
human2.say('чёткий чел->')

print(human1.name)
print(human2.name,human2.weight)


class Car:
    def __init__(self,engine, tank_volume,wheels,brand,Colour,speed = 0):
        self.engine = engine
        self.__tank_volume = tank_volume
        self.__wheels = wheels
        self.__brand = brand
        self.Colour = Colour
        self.speed = speed
       

car1 = Car(4,50,4,"Mercedes","red",2)
print(car1.speed)

class Bro:
    def __init__(self,name,weight,height,chin,hands,legs):
        self.name = name
        self.weight = weight
        self.height = height
        self.__chin = chin
        self.__hands = hands
        self.__legs = legs
        


bro1 = Bro("Лёша",4,80,200,1,5)
print(bro1.name)
print(dir(Bro))