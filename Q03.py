# In question number 3, we've to create a calculator program that perform Addition, Subtraction, Multiplication, Division, and Modulus operations from user input.


print("--- Python Calculator ---\n")
try:
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
except ValueError:
    print("Invalid input! Please enter numeric values only.")
    exit()

addition = num1 + num2
subtraction = num1 - num2
multiplication = num1 * num2

if num2 != 0:
    division = num1 / num2
    modulus = num1 % num2
else:
    division = "Undefined (cannot divide by zero)"
    modulus = "Undefined (cannot divide by zero)"

print("\n" + "=" * 40)
print("             CALCULATOR RESULTS")
print("=" * 40)
print(f"Addition (+)      : {num1} + {num2} = {addition}")
print(f"Subtraction (-)   : {num1} - {num2} = {subtraction}")
print(f"Multiplication (*): {num1} * {num2} = {multiplication}")
print(f"Division (/)      : {num1} / {num2} = {division}")
print(f"Modulus (%)       : {num1} % {num2} = {modulus}")
print("=" * 40)