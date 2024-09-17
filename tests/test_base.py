from BE.calculator_helper import CalculatorHelper
import pytest

class Basetest:
    def setup_method(self, method):
        self.calc = CalculatorHelper()
    def teardown_method(self, method):
        del self.calc
        