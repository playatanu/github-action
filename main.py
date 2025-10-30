import os
import sys

print("Python Script Running from GitHub Actions!")
print(f"Python version: {sys.version}")
print(f"Working directory: {os.getcwd()}")

# Simple function
def calculate(a, b):
    return a + b

result = calculate(15, 25)
print(f"Calculation: 15 + 25 = {result}")

print("Script completed successfully!")