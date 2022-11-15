from car import Car
import random

def main():
    for x in range(4):
        tires = random.randint(0, 4)
        engine = random.randint(0, 1)
        doors = random.randint(0, 1)
        print("====================================================================================================")
        print("Car number: {}".format(x + 1))
        car = Car()
        car.add_tires(tires)
        car.add_engine(engine)
        car.add_doors(doors)
        car.run()
        print("====================================================================================================")
        print("")


if __name__ == "__main__":
    main()
