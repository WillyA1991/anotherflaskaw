""" Testing the calculator operations """
from calculator.operations import Addition, Subtraction, Multiplication, Division


def test_calculator_operations_add():
    """ Testing the Calculator operations add method """
    assert Addition.add(1.0, 2) == 3


def test_calculator_operations_subtract():
    """ Testing the Calculator operations subtract method """
    assert Subtraction.subtract(1.0, 2) == -1.0


def test_calculator_operations_multiply():
    """ Testing the Calculator operations multiply method """
    assert Multiplication.multiply(1.0, 2) == 2.0


def test_calculator_operations_divide():
    """ Testing the Calculator operations divide method """
    assert Division.divide(1.0, 2) == 0.5
    assert Division.divide(6.0, 2) == 3.0
    assert Division.divide(1.0, 0) == "Cannot divide by 0"
