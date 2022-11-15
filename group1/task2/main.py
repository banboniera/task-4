from operations import (Addition, Division, Multiplication, Operation,
                        Subtraction)


def main():
    operations = []  # type: list[Operation]
    operations.append(Addition)
    operations.append(Subtraction)
    operations.append(Multiplication)
    operations.append(Division)

    first_number = 0
    second_number = 0
    not_numeric = True

    print("====================================================================================================")
    print("")

    while (not_numeric):
        print("Please provide first number: ", end="")
        first_number = input()
        not_numeric = not first_number.isnumeric()

    not_numeric = True

    while (not_numeric):
        print("Please provide second number: ", end="")
        second_number = input()
        not_numeric = not second_number.isnumeric()

    operation = ""
    while (operation not in ["+", "-", "*", "/"]):
        print("Please provide operation (+, -, *, /): ", end="")
        operation = input()

    for op in operations:
        op.calculate(operation, first_number, second_number)

    print("")
    print("====================================================================================================")


if __name__ == "__main__":
    main()
