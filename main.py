import os
import sys

print("🚀 Python Script Running from GitHub Actions!")
print(f"Python version: {sys.version}")
print(f"Working directory: {os.getcwd()}")

# Simple function
def calculate(a, b):
    return a + b

result = calculate(15, 25)
print(f"Calculation: 15 + 25 = {result}")

# Create a file
with open('success.txt', 'w') as f:
    f.write(f'Success! Python {sys.version.split()[0]} ran on GitHub Actions!')
    f.write(f'\nCalculation result: {result}')

print("✅ Script completed successfully!")
print("✅ Created success.txt file")