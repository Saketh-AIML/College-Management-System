from database import db

def add_fac():

    name=input("Enter the name of faculty: ")
    email=input("Enter the email id: ")
    phone=input("Enter the Phone number: ")
    department=input("Enter the Department: ")

    cursor=db.cursor()
    query=""" 
    INSERT INTO faculty
    (faculty_name,email,phone,department)
    values(%s,%s,%s,%s)  
    """
    values=(name,email,phone,department)

    cursor.execute(query,values)

    db.commit()

    print("Faculty added successfully")

    cursor.close()

def view_fac():

    cursor=db.cursor()

    cursor.execute("SELECT * FROM faculty")

    data=cursor.fetchall()

    for i in data:
        print(i)

    cursor.close()

def update_fac():

    faculty_id=int(input("Enter faculty id: "))

    name=input("Enter the name: ")
    email=input("Enter the email: ")
    phone=input("Enter the phone number: ")
    department=input("Enter the department: ")

    cursor=db.cursor()

    query="""
    UPDATE faculty 
    SET 
    faculty_name=%s,
    email=%s,
    phone=%s,
    department=%s
    WHERE faculty_id=%s
"""
    values=(name,email,phone,department,faculty_id)

    cursor.execute(query,values)

    db.commit()

    print("Faculty updated successfully")

    cursor.close()

def del_fac():

    print("Delete requires Authorized access")

def faculty_menu():

    while(True):
       print("\n===== FACULTY MANAGEMENT =====")
       print("1. Add Faculty")
       print("2. View Faculty")
       print("3. Update Faculty")
       print("4. Delete Faculty")
       print("5. Exit")

       choice=int(input("Enter your Choice: "))

       if choice==1 :
         add_fac()

       elif choice==2 :
           view_fac()

       elif choice==3:
           update_fac()

       elif choice==4:
           del_fac()

       elif choice==5:
           break

       else:
           print("Invalid choice")



