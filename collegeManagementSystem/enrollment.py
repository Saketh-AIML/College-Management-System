from database import db

def add_enrollment():

    student_id=int(input("Enter the student id: "))
    course_id=int(input("Enter the course id: "))
    enrollment_date=input("Enter the enrollment date: ")

    cursor=db.cursor()

    query="""
    INSERT INTO enrollments
    (student_id,course_id,enrollment_date)
    VALUES
    (%s,%s,%s)    
"""
    values=(student_id,course_id,enrollment_date)

    cursor.execute(query,values)

    db.commit()

    print("Enrollment added successful")

    cursor.close()

def view_enrollment():

    cursor=db.cursor()

    cursor.execute("SELECT * FROM enrollments")

    data = cursor.fetchall()

    for i in data :
        print(i)

    cursor.close()

def update_enrollment():

    enrollment_id=int(input("Enter the enrollment id: "))

    student_id=int(input("Enter the student id: "))
    course_id=int(input("Enter the course id :"))
    enrollment_date=input("Enter the enrollment date: ")

    cursor=db.cursor()

    query="""
    UPDATE enrollments SET
    student_id=%s,
    course_id=%s,
    enrollment_date=%s

    WHERE enrollment_id=%s
    
"""
    values=(student_id,course_id,enrollment_date,enrollment_id)

    cursor.execute(query,values)

    db.commit()

    print("Enrollment updated successfully")

    cursor.close()


def delete_enrollment():

    print("Delete requires Authorized access")


def enrollment_menu():

    while(True):

        print("\n===== ENROLLMENT =====")
        print("1. Add enrollment")
        print("2. View enrollment")
        print("3. Update enrollment")
        print("4. Delete enrollment")
        print("5. Exit")

        choice=int(input("Enter your Choice: "))
        
        if choice==1 :
            add_enrollment()
        
        elif choice==2 :
            view_enrollment()
        
        elif choice==3:
            update_enrollment()
        
        elif choice==4:
            delete_enrollment()
        
        elif choice==5:
            break
        
        else:
            print("Invalid choice")
        
