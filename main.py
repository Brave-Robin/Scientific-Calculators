import math

"""
Just another `calculator` yet
"""

'''
addition
subtraction — вычитание
multiplication — умножение
division
'''


def addition(first, second):
    """
    :param first: int or float
    :param second: int or float
    :return: the summ of first and second
    """
    return first + second


def subtraction(first, second):
    """
    :param first: int or float
    :param second: int or float
    :return:
    """
    return first - second


def multiplication(first, second):
    """
    :param first: int or float
    :param second: int or float
    :return:
    """
    return first * second


def division(first, second):
    """
    :param first: int or float
    :param second: int or float
    :return:
    """
    return first / second


def interact():
    """
    :return:
    """
    print("Enter digit and choice operation type")
    first = float(input("Write first: "))
    second = float(input("Write second: "))
    operation = str(input("Write operation type (+, -, *, /): "))

    if operation == "+":
        return addition(first, second)
    elif operation == "-":
        return subtraction(first, second)
    elif operation == "*":
        return multiplication(first, second)
    elif operation == "/":
        return division(first, second)
    else:
        print("Somthing wrong - fallback!")
        exit(1)


if __name__ == '__main__':
    print(interact())