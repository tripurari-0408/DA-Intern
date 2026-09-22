# In question number 2, we'll take different data types as input and display their values along with their data types.

age = int(input("Enter your age: "))          # (Integer)
cgpa = float(input("Enter your CGPA: "))      # (Float)
name = input("Enter your name: ")            # (String)
is_enrolled = input("Are you enrolled? (True/False): ") == "True"  # (Boolean)

print(f"Value: {age} \t\t Data Type: {type(age)}")
print(f"Value: {cgpa} \t\t Data Type: {type(cgpa)}")
print(f"Value: {name} \t\t Data Type: {type(name)}")
print(f"Value: {is_enrolled} \t Data Type: {type(is_enrolled)}")