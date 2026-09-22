# Here, in  this question, we've to Print a welcome message.
# Next we'll take your Name, College Name and Branch as input and displays the entered information in a formatted output.

print("Welcome! Please enter your details:")
name = input("Enter your Name: ")
college_name = input("Enter your College Name: ")
branch = input("Enter your Branch: ")

print("=" * 40)
print("          STUDENT PROFILE")
print("=" * 40)
print(f"Name         : {name}")
print(f"College Name : {college_name}")
print(f"Branch       : {branch}")
print("=" * 40)