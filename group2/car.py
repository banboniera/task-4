

class Car:
    tires = 0
    engine = False
    doors = False

    def add_tires(self, amount: int):
        self.tires = amount

    def add_engine(self, value: bool):
        self.engine = value

    def add_doors(self, value: bool):
        self.doors = value

    def run(self):
        if self.tires < 4:
            print("Car can not go on {} tires".format(self.tires))
            return

        if not self.engine:
            print("Car can not go without engine")
            return

        if not self.doors:
            print("You can not enter a car without doors")
            return

        print("Car is going...")
