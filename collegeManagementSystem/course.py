from database import db

def add_course():

    course_name=input("Enter the course name: ")
    course_id=int(input("Enter the course id: "))
    credits=int(input("Enter the credits: "))
    department=input("Enter the department: ")
    faculty_id=int(input("Enter the faculty id: "))
    semester=int(input("Enter the semester: "))

    cursor=db.cursor()
    query="""
    INSERT INTO courses 
    (course_name,credits,department,faculty_id,semester)
    VALUES
    (%s,%s,%s,%s,%s)
    """
    values=(course_name,course_id,credits,department,faculty_id,semester)

    cursor.execute(query,values)

    db.commit()

    print("Course added Successfully")

    cursor.close()
    
def view_course():

    cursor=db.cursor()

    cursor.execute("SELECT * FROM courses")

    data=cursor.fetchall()

    for i in data:
        print(i)

    cursor.close()

def update_course():

    course_id=int(input("Enter the course id: "))

    course_name=input("Enter the courses name: ")
    credits=int(input("Enter the credits: "))
    department=input("Enter the department: ")
    faculty_id=int(input("Enter the faculty id: "))
    semester=int(input("Enter the semester: "))

    cursor=db.cursor()

    query="""
    UPDATE course 
    SET course_name=%s,
    credits=%s,
    department=%s,
    faculty_id=%s,
    semester=%s
    WHERE course_id=%s
"""
    values=(course_name,credits,department,faculty_id,semester,course_id)

    cursor.execute(query,values)

    db.commit()

    print("Course updates successfully")

    cursor.close()

def delete_course():
    print("Delete requires Authorized access")


def course_menu():

    while(True):

        print("\n===== COURSE MANAGEMENT =====")
        print("1. Add course")
        print("2. View course")
        print("3. Update course")
        print("4. Delete course")
        print("5. Exit")

        choice=int(input("Enter your choice: "))

        if choice==1:
            add_course()

        elif choice==2:
            view_course()

        elif choice==3:
            update_course()

        elif choice==4:
            delete_course()

        elif choice==5:
            break

        else:
            print("Enter a vaild choice")

