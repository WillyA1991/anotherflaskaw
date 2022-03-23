"""Calculation and Addition, Multiplication, and Subtraction Classes"""
from calculator.operations import Addition as Add, Subtraction as Sub, Multiplication as Mult, \
    Division as Div


class Calculation:
    """calculation abstract base class"""

    # pylint: disable=too-few-public-methods
    def __init__(self, tuple_list: tuple):
        """ constructor method """
        self.values = Calculation.convert_args_to_tuple_of_float(tuple_list)

    @classmethod
    def create(cls, tuple_list: tuple):
        """ factory method """
        return cls(tuple_list)

    @staticmethod
    def convert_args_to_tuple_of_float(tuple_list):
        """ standardize values to list of floats """
        # lists can be modified and tuple cannot, tuple are faster.
        # We need to convert the tuple of potentially random data types (its raw data)
        # into a standard data format to keep things consistent
        # so we convert it to float
        # then make it a tuple again because you actually won't need to
        # change the calculation values
        # can also use it as a list and then would be able to edit the calculation
        list_values_float = []
        for item in tuple_list:
            list_values_float.append(float(item))
        return tuple(list_values_float)


class Addition(Calculation):
    """calculation addition class"""

    def get_result(self):
        """returns the results of the addition"""
        sum_of_values = 0.0
        for value in self.values:
            sum_of_values = Add.add(value, sum_of_values)
        return sum_of_values


class Multiplication(Calculation):
    """calculation multiplication class"""

    def get_result(self):
        """returns the results of the multiplication"""
        mult_of_values = 1.0
        for value in self.values:
            mult_of_values = Mult.multiply(value, mult_of_values)
        return mult_of_values


class Subtraction(Calculation):
    """calculation subtraction class"""

    def get_result(self):
        """returns the results of the subtraction"""
        difference_of_values = 0.0
        for value in self.values:
            difference_of_values = Sub.subtract(difference_of_values, value)
        return difference_of_values


class Division(Calculation):
    """calculation division class"""

    def get_result(self):
        """returns the results of the division"""
        division_of_values = 1.0
        for value in self.values:
            try:
                division_of_values = Div.divide(division_of_values, value)
            except ZeroDivisionError:
                return "Cannot divide by 0"
        return division_of_values
