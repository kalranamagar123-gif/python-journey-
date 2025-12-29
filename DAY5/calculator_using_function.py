#Create functions for each operation
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b != 0:
     return a / b
    else:
     return "cannot divide by zero"


num1 = 12
num2 = 2
print("addition", add(num1, num2))
print("subtraction", subtract(num1, num2))
print("multiplication", multiply(num1, num2))
print("division", divide(num1, num2))



#Calculator with user input
number1 = float(input("Enter a first number:"))
number2 = float(input("Enter second number: "))
operation = input("Enter operations: +,-,*,/")

if operation == "+":
   print("addition = ", add(number1, number2))
elif operation == "-":
   print("Subtraction = ", subtract(number1, number2))
elif operation == "*":
   print("Multiplication = ", multiply(number1, number2))
elif operation == "/":
   print("division = ", divide(number1, number2))
else:
   print("invalid operation")

