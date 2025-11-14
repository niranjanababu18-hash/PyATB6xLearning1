class Calculator:
    # Parameterized constructor
    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2

    # Method to calculate sum
    def add(self):
        return self.num1 + self.num2

    # Method to calculate multiplication
    def multiply(self):
        return self.num1 * self.num2


calc = Calculator(10, 5)
print("Sum:", calc.add())  # Prints sum
print("Product:", calc.multiply())
