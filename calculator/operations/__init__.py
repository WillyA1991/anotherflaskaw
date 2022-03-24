""" These are the Operation classes """
# pylint: disable=too-few-public-methods

class Addition:
    """Operations addition class"""
    @staticmethod
    def add(value_1, value_2):
        """Add method"""
        return value_1 + value_2


class Subtraction:
    """Operations subtraction class"""
    @staticmethod
    def subtract(value_1, value_2):
        """Subtraction method"""
        return value_1 - value_2


class Multiplication:
    """Operations multiplication class"""
    @staticmethod
    def multiply(value_1, value_2):
        """Multiplication method"""
        return value_1 * value_2


class Division:
    """Operations division class"""
    @staticmethod
    def divide(value_1, value_2):
        """Division method"""
        try:
            return value_1 / value_2
        except ZeroDivisionError:
            return "Cannot divide by 0"
