class Calculator:
    def add(self, a, b):
        """Add two numbers"""
        return a + b

    def subtract(self, a, b):
        """Subtract two numbers"""
        return a - b

    def multiply(self, a, b):
        """Multiply two numbers"""
        return a * b

    def divide(self, a, b):
        """Divide two numbers"""
        if b == 0:
            raise ValueError("Division by zero is not allowed")
        return a / b

    def power(self, base, exponent):
        """Calculate power of a number"""
        return base ** exponent


class AdvancedCalculator(Calculator):
    def factorial(self, n):
        """Calculate factorial of a number"""
        if n < 0:
            raise ValueError("Factorial is not defined for negative numbers")
        if n == 0:
            return 1
        result = 1
        for i in range(1, n + 1):
            result *= i
        return result

    def is_prime(self, n):
        """Check if a number is prime"""
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True