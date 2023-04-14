class Animal:
    def __init__(self,name):
      self.myname=name
    def talk(self):
      raise NotImplementedError("Subclass must implement abstract method")

class Cat(Animal):
    def talk(self):
        return  "Meow"
class Dog(Animal):
    def talk(self):
        return "Woof"

class Horse(Animal):
    def talk(self):
        return "Blutters"
class Donkey(Animal):
    def talk(self):
        return "Neighs"


paka=Cat("Whiskers")
mbwa=Dog("Musty")
hos=Horse("Tonka")
don=Donkey("Dora")
print(paka.myname+" :" + paka.talk())
print(mbwa.myname+" :" + mbwa.talk())
print(hos.myname+" :" + hos.talk())
print(don.myname+" :" + don.talk())