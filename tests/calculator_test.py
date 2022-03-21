""" Testing the Calculator """
from calculator import Calculator


def tuple_list():
    """ Arrange data for AAA testing """
    return 1.0, 2


def test_calculator_add_method():
    """ Testing the calculator add method """
    # this is shown using the calculator object add method
    result = Calculator.add(tuple_list())
    assert result == 3.0


def test_calculator_subtract_method():
    """ Testing the calculator subtract method """
    assert Calculator.subtract(tuple_list()) == -3.0


def test_calculator_multiply_method():
    """ Testing the calculator multiply method """
    assert Calculator.multiply(tuple_list()) == 2.0
