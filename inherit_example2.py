class Magari:
    def __init__(self, make, model, year):
        self.mymake = make
        self.mymodel = model
        self.myyear = year

    def kuanzisha(self):
        print(f"{self.mymake}{self.mymodel}{self.myyear} started")


class toyota(Magari):
    def __init__(self, make, model, year, num_doors):
        super().__init__(make, model, year)
        self.mynum_door = num_doors

    def kuanzisha(self):
        print(f"{self.mymake} {self.mymodel} car with {self.mynum_door} doors started")


gari = toyota("Premio", "Saloon", 2023, 5)
gari.kuanzisha()


# create a class of motorcycle make model year engine size

class Motorcycles(Magari):
    def __init__(self, make, model, year, eng_cc):
        super().__init__(make, model, year)
        self.myeng_cc = eng_cc

    def kuanza(self):
        print(f"{self.mymake} {self.mymodel} {self.myyear} model with {self.myeng_cc}cc started")


nduthi = Motorcycles("Kawasaki", "Dirt Bike", 2013, 250)
nduthi.kuanza()
