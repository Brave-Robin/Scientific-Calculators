"""
Just another `calculator` yet
"""

import sys


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
    if operation == "-":
        return subtraction(first, second)
    if operation == "*":
        return multiplication(first, second)
    if operation == "/":
        return division(first, second)
    print("Somthing wrong - fallback!")
    sys.exit(1)


if __name__ == '__main__':
    print(interact())
