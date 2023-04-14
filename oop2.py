class Person:
    def __init__(self, name, age):
        self.myname = name
        self.myage = age

    def habari(self):
        print("Hello,My name is " + self.myname)


class Student(Person):
    def __init__(self,name,age,student_id):
        super().__init__(name,age)
        self.mystudent=student_id
        self.myage=age
    def habari(self):
        super().habari()
        print("Im a student with ID"+str(self.mystudent)+" Im "+ str(self.myage)+" Years old")
myname=Student("Joe",18,59911)
myname.habari()

