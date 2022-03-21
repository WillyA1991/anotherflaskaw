""" Testing the calculations classes within the calculator """
from calculator.calculations import Addition, Subtraction, Multiplication, Division


def test_calculation_multiplication_instance():
    """ Testing the Calculator calculations Multiplication """
    tuple_list = (1, 2)
    calculation = Multiplication.create(tuple_list)
    assert isinstance(calculation, Multiplication)

def test_calculation_subtraction_instance():
    """ Testing the Calculator calculations Subtraction """
    tuple_list = (1, 2)
    calculation = Subtraction.create(tuple_list)
    assert isinstance(calculation, Subtraction)

def test_calculation_addition_instance():
    """ Testing the Calculator calculations Addition """
    tuple_list = (1, 2)
    calculation = Addition.create(tuple_list)
    assert isinstance(calculation, Addition)

def test_calculation_division_instance():
    """ Testing the Calculator calculations Division """
    tuple_list = (1, 2)
    calculation = Division.create(tuple_list)
    assert isinstance(calculation, Division)


def test_calculation_add_get_result_method():
    """ Testing the Calculator calculations add method """
    # this is shown using the calculator object add method
    tuple_list = (1.0, 2)
    calculation = Addition.create(tuple_list)
    assert calculation.get_result() == 3.0


def test_calculation_subtract_get_result_method():
    """ Testing the Calculator calculations subtract method """
    tuple_list = (1.0, 2)
    calculation = Subtraction.create(tuple_list)
    assert calculation.get_result() == -3.0


def test_calculation_multiply_get_result_method():
    """ Testing the Calculator calculations multiply method """
    tuple_list = (1.0, 2)
    calculation = Multiplication.create(tuple_list)
    assert calculation.get_result() == 2.0


def test_calculation_divide_get_result_method_1():
    """ Testing the Calculator calculations divide method """
    tuple_list = (1.0, 2)
    calculation = Division.create(tuple_list)
    assert calculation.get_result() == 0.5


def test_calculation_divide_get_result_method_2():
    """ Testing the Calculator calculations divide method when dividing by 0 """
    tuple_list = (1.0, 0)
    calculation = Division.create(tuple_list)
    assert calculation.get_result() == "Cannot divide by 0"
