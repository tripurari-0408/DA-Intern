# Here we've to create two user-defined functions:
# Function to calculate the square of a number.
# Function to calculate the average of three numbers.

def square(n):
    return n * n

def average(a, b, c):
    return (a + b + c) / 3

num = float(input("Enter a number to find its square: "))
print("Square:", square(num))

print("Enter three numbers to find their average:")
n1, n2, n3 = map(float, input("Enter these numbers separated by comma(,) : ").split(','))
print("Average:", average(n1, n2, n3))