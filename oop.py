class Fruits:
    def __init__(self, type, color, price):
        self.mytype = type
        self.mycolor = color
        self.myprice = price

    def onyesha(self):
        print(self.mytype, self.mycolor, self.myprice)


# create an object
myobject = Fruits("Banana", "Yellow", 20)
myobject.onyesha()
obj = Fruits("Mango", "green", 30)
obj.onyesha()
obj1 = Fruits("Watermelon", "green", 100)
obj1.onyesha()
obj2 = Fruits("Orane", "orange", 50)
obj2.onyesha()


class Employees:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def show(self):
        print("Name:" , self.name, "-" +"Salary paid:" , self.salary)


object0 = Employees("Joe", 200000)
object0.show()
object1 = Employees("Erick", 100000)
object1.show()
object2 = Employees("Abdul", 500000)
object2.show()
object3 = Employees("Angel", 300000)
object3.show()
object4 = Employees("Shantell", 250000)
object4.show()
object5 = Employees("Sophie", 400000)
object5.show()
