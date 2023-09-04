#Task 2: To make a calculator to perform basic arithmetic operations
a = int(input("Enter first number: "))
operator = input("Enter the operator{+,-,*,/,%} to perform the operation you want: ")
b = int(input("Enter second number: "))
if operator == "+":
    print("Sum of these two numbers is: ", a + b)
elif operator == "-":
    print("Result of subtraction of above numbers is: ",a - b)
elif operator == "*":
    print("Product of these numbers is: ",a * b)
elif operator == "/":
    print("Result of division of above numbers is :",a / b)
elif operator == "%":
    print("Result of modulus of above two numbers is :",a % b)
else:
    print("Invalid operator or invalid numbers ")