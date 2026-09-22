# Here, we'll demonstrate various Python concepts including string operations, list operations, tuple creation and indexing, dictionary usage and set operations.


# 1. Str Operations
text = "Hello, Python World!"
print("Original:", text)
print("Uppercase:", text.upper())
print("Lowercase:", text.lower())
print("Replace:", text.replace("World", "Universe"))
print("Find 'Python':", text.find("Python"))



# 2. List Operations (Mutable)
fruits = ["apple", "banana"]
fruits.append("cherry")
print("After append:", fruits)
fruits.remove("banana")
print("After remove:", fruits)
fruits.sort()
print("After sort:", fruits)



# 3. Tuple Operations (Immutable)
colors = ("red", "green", "blue")
print("Tuple:", colors)
print("Index 1:", colors[1])



# 4. Dictionary Storing Student Information
student = {
    "name": "Alex",
    "age": 20,
    "branch": "Computer Science"
}
print("Student Dictionary:", student)
print("Student Name:", student["name"])



# 5. Set Operations (Unique, unordered elements)
unique_numbers = {1, 2, 3}
unique_numbers.add(4)
print("After add:", unique_numbers)
unique_numbers.remove(2)
print("After remove:", unique_numbers)