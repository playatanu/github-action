import pytest
from src.calculator import Calculator, AdvancedCalculator


class TestCalculator:
    def setup_method(self):
        self.calc = Calculator()

    def test_add(self):
        assert self.calc.add(2, 3) == 5
        assert self.calc.add(-1, 1) == 0
        assert self.calc.add(0, 0) == 0

    def test_subtract(self):
        assert self.calc.subtract(5, 3) == 2
        assert self.calc.subtract(0, 5) == -5

    def test_multiply(self):
        assert self.calc.multiply(4, 3) == 12
        assert self.calc.multiply(0, 100) == 0

    def test_divide(self):
        assert self.calc.divide(10, 2) == 5
        assert self.calc.divide(5, 2) == 2.5

    def test_divide_by_zero(self):
        with pytest.raises(ValueError, match="Division by zero is not allowed"):
            self.calc.divide(10, 0)

    def test_power(self):
        assert self.calc.power(2, 3) == 8
        assert self.calc.power(5, 0) == 1


class TestAdvancedCalculator:
    def setup_method(self):
        self.advanced_calc = AdvancedCalculator()

    def test_factorial(self):
        assert self.advanced_calc.factorial(0) == 1
        assert self.advanced_calc.factorial(1) == 1
        assert self.advanced_calc.factorial(5) == 120

    def test_factorial_negative(self):
        with pytest.raises(ValueError, match="Factorial is not defined for negative numbers"):
            self.advanced_calc.factorial(-1)

    def test_is_prime(self):
        assert self.advanced_calc.is_prime(2) == True
        assert self.advanced_calc.is_prime(17) == True
        assert self.advanced_calc.is_prime(4) == False
        assert self.advanced_calc.is_prime(1) == False

    def test_inheritance(self):
        # Test that AdvancedCalculator inherits from Calculator
        assert isinstance(self.advanced_calc, Calculator)
        assert self.advanced_calc.add(2, 3) == 5