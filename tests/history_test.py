""" Testing the Calculator history calculations """
import pytest
from calculator.history import Calculations as History
from calculator.calculations import Addition


@pytest.fixture
def clear_history_fixture():
    """ define a function that will run each time you pass it to a test, it is called a fixture """
    # pylint: disable=redefined-outer-name
    History.clear_history()


@pytest.fixture
def setup_addition_calculation_fixture():
    """ define a function that will run each time you pass it to a test, it is called a fixture """
    # pylint: disable=redefined-outer-name
    values = (1.0, 2)
    addition = Addition(values)
    History.add_calculation(addition)


def test_add_calculation_to_history(clear_history_fixture, setup_addition_calculation_fixture):
    """ Testing add calculation to history returns true for success """
    # pylint: disable=unused-argument,redefined-outer-name,singleton-comparison
    assert History.count_history() == 1


def test_clear_calculation_history(clear_history_fixture, setup_addition_calculation_fixture):
    """ Testing clear history method """
    # pylint: disable=unused-argument,redefined-outer-name,singleton-comparison
    assert History.count_history() == 1
    History.clear_history()
    assert History.count_history() == 0
    assert History.clear_history() == True


def test_get_calculation(clear_history_fixture, setup_addition_calculation_fixture):
    """ Test getting a specific calculation out of the history method """
    # pylint: disable=unused-argument,redefined-outer-name
    assert History.get_calculation(0).get_result() == 3.0


def test_get_calc_last_result_value(clear_history_fixture, setup_addition_calculation_fixture):
    """ Test getting the last calculation from the history method """
    # pylint: disable=unused-argument,redefined-outer-name
    assert History.get_last_calculation_result_value() == 3.0


def test_get_calculation_first(clear_history_fixture, setup_addition_calculation_fixture):
    """ Test getting the first calculation from the history method """
    # pylint: disable=unused-argument,redefined-outer-name
    assert History.get_first_calculation().get_result() == 3.0


def test_history_count(clear_history_fixture, setup_addition_calculation_fixture):
    """ Test getting the count of calculations from the history method """
    # pylint: disable=unused-argument,redefined-outer-name
    assert History.count_history() == 1


def test_add_calculation(clear_history_fixture, setup_addition_calculation_fixture):
    """ Test adding a new calculation to the history via append function at the end of the list"""
    # pylint: disable=unused-argument,redefined-outer-name
    History.add_calculation(1.0 + 4)
    assert History.count_history() == 2


def test_get_calc_last_result_object(clear_history_fixture, setup_addition_calculation_fixture):
    """ Test getting the last calculation from the history """
    # pylint: disable=unused-argument,redefined-outer-name
    # This test is if it returns the last calculation as an object
    assert isinstance(History.get_last_calculation_object(), Addition)


def test_add_addition_calculation(clear_history_fixture, setup_addition_calculation_fixture):
    """Test adding an addition calculation to the history"""
    # pylint: disable=unused-argument,redefined-outer-name
    # Test to see if history is updated with the addition calculation
    value1 = 1
    value2 = 2.0
    History.add_addition_calculation(value1, value2)
    assert History.count_history() == 2
    assert History.get_last_calculation_object() == 3


def test_add_subtraction_calculation(clear_history_fixture, setup_addition_calculation_fixture):
    """Test adding an addition calculation to the history"""
    # pylint: disable=unused-argument,redefined-outer-name
    # Test to see if history is updated with the addition calculation
    History.clear_history()
    value1 = 1
    value2 = 2.0
    History.add_subtraction_calculation(value1, value2)
    assert History.count_history() == 1
    assert History.get_last_calculation_object() == -1


def test_add_multiplication_calculation(clear_history_fixture, setup_addition_calculation_fixture):
    """Test adding an addition calculation to the history"""
    # pylint: disable=unused-argument,redefined-outer-name
    # Test to see if history is updated with the addition calculation
    History.clear_history()
    value1 = 1
    value2 = 2.0
    History.add_multiplication_calculation(value1, value2)
    assert History.count_history() == 1
    assert History.get_last_calculation_object() == 2


def test_add_division_calculation(clear_history_fixture, setup_addition_calculation_fixture):
    """Test adding an addition calculation to the history"""
    # pylint: disable=unused-argument,redefined-outer-name
    # Test to see if history is updated with the addition calculation
    History.clear_history()
    value1 = 1
    value2 = 2.0
    History.add_division_calculation(value1, value2)
    assert History.count_history() == 1
    assert History.get_last_calculation_object() == 0.5


def test_add_division_calculation_2(clear_history_fixture, setup_addition_calculation_fixture):
    """Test adding an addition calculation to the history"""
    # pylint: disable=unused-argument,redefined-outer-name,assert-on-string-literal
    # Test to see if history is updated with the addition calculation
    History.clear_history()
    value1 = 1.0
    value2 = 0
    History.add_division_calculation(value1, value2)
    assert "Cannot divide by 0"
