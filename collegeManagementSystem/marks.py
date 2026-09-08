from database import db


def add_marks():

    student_id = int(input("Enter the student id: "))
    course_id = int(input("Enter the course id: "))
    marks = float(input("Enter the marks: "))
    grade = input("Enter the grade: ")

    cursor = db.cursor()

    query = """
    INSERT INTO marks
    (student_id, course_id, marks, grade)
    VALUES
    (%s, %s, %s, %s)
    """

    values = (student_id, course_id, marks, grade)

    cursor.execute(query, values)

    db.commit()

    print("Marks added successfully")

    cursor.close()


def view_marks():

    cursor = db.cursor()

    cursor.execute("SELECT * FROM marks")

    data = cursor.fetchall()

    for i in data:
        print(i)

    cursor.close()


def update_marks():

    mark_id = int(input("Enter the mark id: "))

    student_id = int(input("Enter the student id: "))
    course_id = int(input("Enter the course id: "))
    marks = float(input("Enter the marks: "))
    grade = input("Enter the grade: ")

    cursor = db.cursor()

    query = """
    UPDATE marks SET
    student_id=%s,
    course_id=%s,
    marks=%s,
    grade=%s
    WHERE mark_id=%s
    """

    values = (student_id, course_id, marks, grade, mark_id)

    cursor.execute(query, values)

    db.commit()

    print("Marks updated successfully")

    cursor.close()


def delete_marks():

    print("Delete requires Authorized access")


def marks_menu():

    while(True):

        print("\n===== MARKS MANAGEMENT =====")
        print("1. Add Marks")
        print("2. View Marks")
        print("3. Update Marks")
        print("4. Delete Marks")
        print("5. Exit")

        choice = int(input("Enter your Choice: "))

        if choice == 1:
            add_marks()

        elif choice == 2:
            view_marks()

        elif choice == 3:
            update_marks()

        elif choice == 4:
            delete_marks()

        elif choice == 5:
            break

        else:
            print("Invalid choice")


