from student import student_menu
from faculty import faculty_menu
from course import course_menu
from enrollment import enrollment_menu
from marks import marks_menu
from attendance import attendance_menu

def main_menu():

    while(True):

        print("\n===== COLLEGE MANAGEMENT SYSTEM =====")
        print("1. Student Management")
        print("2. Faculty Management")
        print("3. Course Management")
        print("4. Enrollment Management")
        print("5. Marks Management")
        print("6. Attendance Management")
        print("7. Exit")

        choice = int(input("Enter your Choice: "))

        if choice == 1:
            student_menu()

        elif choice == 2:
            faculty_menu()

        elif choice == 3:
            course_menu()

        elif choice == 4:
            enrollment_menu()

        elif choice == 5:
            marks_menu()

        elif choice == 6:
            attendance_menu()

        elif choice == 7:
            print("Thank you for using College Management System")
            break

        else:
            print("Invalid choice")


main_menu()