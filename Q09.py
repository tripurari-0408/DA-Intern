# In this question, we'll create a simple student record management system using Python. The system will allow users to CREATE, READ, UPDATE, and DELETE student records.

students = []

while True:
    print("1. Add Student")
    print("2. Display All Students")
    print("3. Search Student by Name")
    print("4. Delete Student Record")
    print("5. Exit")
    
    choice = input("Enter your choice (1-5): ")
    
    if choice == '1':
        name = input("Enter Student Name: ")
        age = input("Enter Student Age: ")
        branch = input("Enter Branch: ")
        
        student = {"name": name, "age": age, "branch": branch}
        students.append(student)
        print("-> Student added successfully!")
        
    elif choice == '2':
        if not students:
            print("-> No student records found.")
        else:
            print("\n--- All Student Records ---")
            for i, s in enumerate(students, 1):
                print(f"{i}. Name: {s['name']} | Age: {s['age']} | Branch: {s['branch']}")
                
    elif choice == '3':
        search_name = input("Enter name to search: ")
        found = False
        print("\n--- Search Results ---")
        for s in students:
            if s['name'].lower() == search_name.lower():
                print(f"Name: {s['name']} | Age: {s['age']} | Branch: {s['branch']}")
                found = True
        if not found:
            print("-> Student not found.")
            
    elif choice == '4':
        del_name = input("Enter the name of the student to delete: ")
        found = False
        for s in students:
            if s['name'].lower() == del_name.lower():
                students.remove(s)
                print("-> Student record deleted successfully!")
                found = True
                break
        if not found:
            print("-> Student not found.")
            
    elif choice == '5':
        print("Exiting Student Record System. Goodbye!")
        break
        
    else:
        print("-> Invalid choice! Please enter a number between 1 and 5.")