from database import db

def add_student():

    name = input("Enter student name: ")
    email = input("Enter email: ")
    phone = input("Enter phone: ")
    department = input("Enter department: ")
    year = int(input("Enter year: "))

    cursor = db.cursor()

    query = """
    INSERT INTO Students
    (student_name, email, phone, department, year)
    VALUES (%s, %s, %s, %s, %s)
    """

    values = (name, email, phone, department, year)

    cursor.execute(query, values)

    db.commit()

    print("Student added successfully")

    cursor.close()

def view_students():

    cursor = db.cursor()

    cursor.execute("SELECT * FROM Students")

    data = cursor.fetchall()

    for i in data:
        print(i)

    cursor.close()

def update_student():

    student_id = int(input("Enter student id: "))

    name = input("Enter new name: ")
    email = input("Enter new email: ")
    phone = input("Enter new phone: ")
    department = input("Enter new department: ")
    year = int(input("Enter new year: "))

    cursor = db.cursor()

    query = """
    UPDATE Students
    SET student_name=%s,
        email=%s,
        phone=%s,
        department=%s,
        year=%s
    WHERE student_id=%s
    """

    values = (name, email, phone, department, year, student_id)

    cursor.execute(query, values)

    db.commit()

    print("Student updated successfully")

    cursor.close()

def delete_student():
    
    print("Student cannot be deleted.")   



def student_menu():

    while True:

        print("\n===== STUDENT MANAGEMENT =====")
        print("1. Add Student")
        print("2. View Students")
        print("3. Update Student")
        print("4. Delete Student")
        print("5. Exit")

        choice = int(input("Enter your choice: "))

        if choice == 1:
            add_student()

        elif choice == 2:
            view_students()

        elif choice == 3:
            update_student()

        elif choice == 4:
            delete_student()

        elif choice == 5:
            break

        else:
            print("Invalid choice")

