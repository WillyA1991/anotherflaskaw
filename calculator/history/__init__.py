"""Calculation history class for maintaining result posterity"""
from calculator.operations import Addition, Subtraction, Multiplication, Division


class Calculations:
    """Calculations class to manage the history of calculations"""
    history = []

    # pylint: disable=too-few-public-methods
    @staticmethod
    def clear_history():
        """Clears the history of calculations"""
        Calculations.history.clear()
        return True

    @staticmethod
    def count_history():
        """Retrieve the number of results in history at point in time"""
        return len(Calculations.history)

    @staticmethod
    def get_last_calculation_object():
        """Retrieves the last calculation placed into the calculator"""
        return Calculations.history[-1]

    @staticmethod
    def get_last_calculation_result_value():
        """Retrieves the last result of the last calculation placed into the calculator"""
        calculation = Calculations.get_last_calculation_object()
        return calculation.get_result()

    @staticmethod
    def get_first_calculation():
        """Retrieves the first calculation placed into the calculator"""
        return Calculations.history[0]

    @staticmethod
    def get_calculation(num):
        """Retrieves a specifically identified calculation from the history list"""
        return Calculations.history[num]

    @staticmethod
    def add_calculation(calculation):
        """Adds a new calculation to the historical
        list via append function at the end of the list"""
        return Calculations.history.append(calculation)

    @staticmethod
    def add_addition_calculation(value1, value2):
        """Create an addition and add object to history using factory method create"""
        Calculations.add_calculation(Addition.add(value1, value2))
        # Get the result of the calculation
        return True

    @staticmethod
    def add_subtraction_calculation(value1, value2):
        """Create a subtraction and add object to history using factory method create"""
        Calculations.add_calculation(Subtraction.subtract(value1, value2))
        return True

    @staticmethod
    def add_multiplication_calculation(value1, value2):
        """Create a multiplication and add object to history using factory method create"""
        Calculations.add_calculation(Multiplication.multiply(value1, value2))
        return True

    @staticmethod
    def add_division_calculation(value1, value2):
        """Create a division and add object to history using factory method create"""
        Calculations.add_calculation(Division.divide(value1, value2))
        return True
