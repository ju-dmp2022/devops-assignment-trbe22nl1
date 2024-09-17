from BE.calculator_helper import CalculatorHelper
import pytest

class Basetest:
    def setup_method(self, method):
        self.calc = CalculatorHelper()
    def teardown_method(self, method):
        del self.calc

class TestCalculator(Basetest): 
    @pytest.mark.parametrize("a, b, expected", [
        (3, 3, 6),       # Test case 1: 3 + 3 = 6
        (3, -3, 0),      # Test case 2: 3 + (-3) = 0
        (0, 0, 0),       # Test case 3: 0 + 0 = 0
    ])
        #Arrange
    def test_add(self,a ,b, expected):
        #Action
        value = self.calc.add(a,b)
        #Assert     
        assert value == expected, f"Expected {expected} but instead got {value}."
    
    @pytest.mark.parametrize("a, b, expected", [
        (3, 3, 0),       # Test case 1: 3 - 3 = 0
        (3, -3, 6),      # Test case 2: 3 - (-3) = 6
        (0, 0, 0),       # Test case 3: 0 - 0 = 0
    ])

    def test_subtract(self,a ,b ,expected):
        value = self.calc.subtract(a,b)
        assert value == expected, f"Expected {expected} but instead got {value}."

    @pytest.mark.parametrize("a, b, expected", [
        (3, 3, 9),       # Test case 1: 3 * 3 = 9
        (3, -3, -9),      # Test case 2: 3 * (-3) = -9
        (0, 0, 0),       # Test case 3: 0 * 0 = 0
    ])
    def test_multiply(self,a ,b ,expected):
        value = self.calc.multiply(a,b)
        assert value == expected, f"Expected {expected} but instead got {value}."

    @pytest.mark.parametrize("a, b, expected", [
        (3, 3, 1),       # Test case 1: 3 / 3 = 1
        (3, -3, -1),      # Test case 2: 3 / (-3) = -1
        (1, 1, 1),       # Test case 3: 1 / 1 = 1
    ])
    def test_divide(self,a ,b ,expected):
        value = self.calc.divide(a,b)
        assert value == expected, f"Expected {expected} but instead got {value}."

    def test_divide_by_zero(self):
        # Act and Assert
        with pytest.raises(ZeroDivisionError, match=("division by zero")):
            self.calc.divide(1,0)

