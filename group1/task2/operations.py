class Operation:
    def calculate(operation: str, first_number: float, second_number: float):
        pass


class Addition(Operation):
    def calculate(operation, first_number, second_number):
        first_number = float(first_number)
        second_number = float(second_number)
        if operation == "+":
            print("{} + {} = {}".format(first_number,
                  second_number, first_number + second_number))
            return
        pass


class Subtraction(Operation):
    def calculate(operation, first_number, second_number):
        first_number = float(first_number)
        second_number = float(second_number)
        if operation == "-":
            print("{} - {} = {}".format(first_number,
                  second_number, first_number - second_number))
            return
        pass


class Multiplication(Operation):
    def calculate(operation, first_number, second_number):
        first_number = float(first_number)
        second_number = float(second_number)
        if operation == "*":
            print("{} * {} = {}".format(first_number,
                  second_number, first_number * second_number))
            return
        pass


class Division(Operation):
    def calculate(operation, first_number, second_number):
        first_number = float(first_number)
        second_number = float(second_number)
        if operation == "/":
            print("{} / {} = {}".format(first_number,
                  second_number, round(first_number / second_number, 2)))
            return
        pass
