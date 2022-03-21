""" Testing the Calculator """
from calculator import Calculator


def tuple_list_1():
    """ Arrange data for AAA testing """
    return 1.0, 2

def tuple_list_2():
    """ Arrange data for AAA testing of division by 0 """
    return 1.0, 0


def test_calculator_add_method():
    """ Testing the calculator add method """
    # this is shown using the calculator object add method
    result = Calculator.add(tuple_list_1())
    assert result == 3.0


def test_calculator_subtract_method():
    """ Testing the calculator subtract method """
    assert Calculator.subtract(tuple_list_1()) == -3.0


def test_calculator_multiply_method():
    """ Testing the calculator multiply method """
    assert Calculator.multiply(tuple_list_1()) == 2.0


def test_calculator_divide_method_1():
    """ Testing the calculator divide method """
    assert Calculator.divide(tuple_list_1()) == 0.5


def test_calculator_divide_method_2():
    """ Testing the calculator divide method with 0 as denominator """
    assert Calculator.divide(tuple_list_2()) == "Cannot divide by 0"
