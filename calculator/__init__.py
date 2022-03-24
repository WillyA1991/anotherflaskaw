""" This is the Calculator Class """
from calculator.calculations import Addition, Subtraction, Multiplication, Division


class Calculator:
    """Creating the Calculator class"""

    @staticmethod
    def add(tuple_list):
        """add method within the Calculator class"""
        # call the static method add to return the sum and set it to the calculator result property
        calculation = Addition.create(tuple_list)
        return calculation.get_result()

    @staticmethod
    def subtract(tuple_list):
        """subtract method within the Calculator class"""
        calculation = Subtraction.create(tuple_list)
        return calculation.get_result()

    @staticmethod
    def multiply(tuple_list):
        """multiply method within the Calculator class"""
        calculation = Multiplication.create(tuple_list)
        return calculation.get_result()

    @staticmethod
    def divide(tuple_list):
        """divide method within the Calculator class"""
        calculation = Division.create(tuple_list)
        return calculation.get_result()
