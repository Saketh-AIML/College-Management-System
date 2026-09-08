from database import db


def add_attendance():

    student_id = int(input("Enter the student id: "))
    course_id = int(input("Enter the course id: "))
    attendance_date = input("Enter the attendance date: ")
    status = input("Enter the attendance status: ")

    cursor = db.cursor()

    query = """
    INSERT INTO attendance
    (student_id, course_id, attendance_date, status)
    VALUES
    (%s, %s, %s, %s)
    """

    values = (student_id, course_id, attendance_date, status)

    cursor.execute(query, values)

    db.commit()

    print("Attendance added successfully")

    cursor.close()


def view_attendance():

    cursor = db.cursor()

    cursor.execute("SELECT * FROM attendance")

    data = cursor.fetchall()

    for i in data:
        print(i)

    cursor.close()


def update_attendance():

    attendance_id = int(input("Enter the attendance id: "))

    student_id = int(input("Enter the student id: "))
    course_id = int(input("Enter the course id: "))
    attendance_date = input("Enter the attendance date: ")
    status = input("Enter the attendance status: ")

    cursor = db.cursor()

    query = """
    UPDATE attendance SET
    student_id=%s,
    course_id=%s,
    attendance_date=%s,
    status=%s
    WHERE attendance_id=%s
    """

    values = (
        student_id,
        course_id,
        attendance_date,
        status,
        attendance_id
    )

    cursor.execute(query, values)

    db.commit()

    print("Attendance updated successfully")

    cursor.close()


def delete_attendance():

    print("Delete requires Authorized access")


def attendance_menu():

    while(True):

        print("\n===== ATTENDANCE MANAGEMENT =====")
        print("1. Add Attendance")
        print("2. View Attendance")
        print("3. Update Attendance")
        print("4. Delete Attendance")
        print("5. Exit")

        choice = int(input("Enter your Choice: "))

        if choice == 1:
            add_attendance()

        elif choice == 2:
            view_attendance()

        elif choice == 3:
            update_attendance()

        elif choice == 4:
            delete_attendance()

        elif choice == 5:
            break

        else:
            print("Invalid choice")


