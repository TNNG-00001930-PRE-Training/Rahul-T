import unittest

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Error: Division by zero!"
    else:
        return x / y

def calculator():
    while True:
        print("\nCalculator Options:")
        print("1. Addition")
        print("2. Subtraction")
        print("3. Multiplication")
        print("4. Division")
        print("5. Exit")

        choice = input("Enter your choice (1/2/3/4/5): ")

        if choice in ('1', '2', '3', '4'):
            num1 = get_valid_number("Enter first number: ")
            num2 = get_valid_number("Enter second number: ")

            if choice == '1':
                return add(num1, num2)
            elif choice == '2':
                return subtract(num1, num2)
            elif choice == '3':
                return multiply(num1, num2)
            elif choice == '4':
                return divide(num1, num2)
        elif choice == '5':
            print("Exiting the calculator.")
            break
        else:
            print("Error: Invalid input! Please enter a valid option.")

def get_valid_number(prompt):
    while True:
        try:
            num = float(input(prompt))
            return num
        except ValueError:
            print("Error: Please enter a valid number.")

class TestCalculator(unittest.TestCase):

    def test_addition(self):
        self.assertEqual(calculator(), 8)

    def test_subtraction(self):
        self.assertEqual(calculator(), 2)

    def test_multiplication(self):
        self.assertEqual(calculator(), 15)

    def test_division(self):
        self.assertEqual(calculator(), 5)

if __name__ == "__main__":
    unittest.main(argv=[''], exit=False)

