# In this question, we'll have to demonstrate file handling in Python. We'll create a text file, write some content into it and then read the content back.


with open("introduction.txt", "w") as file:
    file.write("""Hello! 
    My name is an Tripurari Kumar.
    I am currently learning Data Analysis from IIT Patna.
    This text was written directly from a Python code!""")

print("File 'introduction.txt' created and written successfully!")
print("--- Reading File Contents ---")
with open("introduction.txt") as file:
    content = file.read()
    print(content)
