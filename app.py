from flask import Flask, request, json 
from flask_sqlalchemy import SQLAlchemy
import psycopg2
from flask_migrate import Migrate

app = Flask(__name__)

# app.config['SQLALCHEMY_DATABASE_URI']='postgresql://postgres:password@localhost:5432/school_db'
# app.config['SQLALCHEMY _TRACT_MODIFICATIONS'] = False

# db=SQLAlchemy(app)
# migrate = Migrate(app, db)



def getconnection(database_name, user_name, user_password, db_host, db_port):
    conn = psycopg2.connect(
        database = database_name,
        user = user_name,
        password = user_password,
        host = db_host,
        port = db_port
    )

    return conn


@app.route('/create_user', methods=["POST"])
def create_user():
    conn = getconnection('school_db', 'postgres', 'password', '127.0.0.1', '5432')
    cursor = conn.cursor()

    if request.method=="POST":
        data = json.loads(request.data,strict=False)
        user = data['username']
        passcode = data['password']

        print(user)
        print(passcode)
        query = "INSERT INTO SOFTWARE_USER(username, password) VALUES(%s, %s)"
        bind = (user, passcode,)
        cursor.execute( query, bind )
        conn.commit()
        conn.close()

        return "User created successfully!!!!"

@app.route('/create_department', methods=["POST"]) 
def create_department():
    conn = getconnection('school_db', 'postgres', 'password', '127.0.0.1', '5432')
    cursor = conn.cursor()

    if request.method=="POST":
        data = json.loads(request.data,strict=False)
        department = data['department']
 
        print(department)

        query = "INSERT INTO DEPARTMENT(DEPARTMENT) VALUES( %s)"
        bind = (department,)
        cursor.execute( query, bind )
        conn.commit()
        conn.close()

    return "done"


@app.route('/create_student', methods=["POST"]) 
def create_student():
    conn = getconnection('school_db', 'postgres', 'password', '127.0.0.1', '5432')
    cursor = conn.cursor()

    if request.method=="POST":
        data = json.loads(request.data,strict=False)
        firstname = data['firstname']
        lastname = data['lastname']
        pg_id = data['pg_id']
        class_id = data['class_id']
        staff_id = data['staff_id']
        
        print(firstname)
        print(lastname)
        print(pg_id)
        print(class_id)
        print(staff_id)
        query = "INSERT INTO STUDENT(FIRSTNAME, LASTNAME, PG_ID, CLASS_ID, STAFF_ID) VALUES( %s, %s, %s, %s, %s)"
        bind = (firstname, lastname, pg_id, class_id, staff_id)
        cursor.execute( query, bind )
        conn.commit()
        conn.close()

    return "done"

@app.route('/create_parent', methods=["POST"])
def create_parent():
    conn = getconnection('school_db', 'postgres', 'password', '127.0.0.1', '5432')
    cursor = conn.cursor()

    if request.method=="POST":
        data = json.loads(request.data,strict=False)
        firstname = data[0]['fname']
        lastname = data[0]['lname']
        phonenumber = data[0]['pnumber']
        email = data[0]['email']
        address = data[0]['address']
        
        print(firstname)
        print(lastname)
        print(phonenumber)
        print(email)
        print(address)

        query = "INSERT INTO PARENT_GUARDIAN(FIRSTNAME, LASTNAME, PHONENUMBER, EMAIL, ADDRESS) VALUES( %s, %s, %s, %s, %s)"
        bind = (firstname, lastname, phonenumber, email, address)
        cursor.execute( query, bind )
        conn.commit()
        conn.close()

    return "done"

@app.route('/create_subject', methods=["POST"])
def create_subject():
    conn = getconnection('school_db', 'postgres', 'password', '127.0.0.1', '5432')
    cursor = conn.cursor()

    if request.method=="POST":
        data = json.loads(request.data,strict=False)
        subject = data['subject']
 
        print(subject)

        query = "INSERT INTO SUBJECTS(SCH_SUBJECTS) VALUES( %s)"
        bind = (subject,)
        cursor.execute( query, bind )
        conn.commit()
        conn.close()

    return "done"


@app.route('/create_staff', methods=["POST"]) 
def create_staff():
    conn = getconnection('school_db', 'postgres', 'password', '127.0.0.1', '5432')
    cursor = conn.cursor()

    if request.method=="POST":
        data = json.loads(request.data,strict=False)
        firstname = data['firstname']
        lastname = data['lastname']
        phonenumber = data['phonenumber']
        email = data['email']
        department = data['department']
        formclass = data['formclass']
        salary = data['salary']
        account = data['accountnum']
        bank = data['bank']
        dob = data['dateofbirth']
        subject = data['subjectteaching']
        address = data['address']
        
        print(firstname)
        print(lastname)
        print(phonenumber)
        print(email)
        print(address)

        query = "INSERT INTO STAFF(FIRSTNAME, LASTNAME, PHONENUMBER, EMAIL, DEPARTMENT, FORMCLASS, SALARY, ACCOUNTNUM, BANK, DATEOFBIRTH, SUBJECTTEACHING, ADDRESS) VALUES( %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
        bind = (firstname, lastname, phonenumber, email, department, formclass, salary, account, bank, dob, subject, address,)
        cursor.execute( query, bind )
        conn.commit()
        conn.close()

    return "done"

@app.route('/all_classes', methods=["GET"])
def all_class():
    conn = getconnection('school_db', 'postgres', 'password', '127.0.0.1', '5432')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM ALL_CLASSES')
    rows = cursor.fetchall()
    print(rows)

    data = []
    for row in rows:
        row_data = {"id": row[0], "class": row[1]}   
        data.append(row_data)

        conn.close()
    return {"classes": data}

@app.route('/all_students', methods=["GET"])
def all_students():
    conn = getconnection('school_db', 'postgres', 'password', '127.0.0.1', '5432')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM STUDENT')
    rows = cursor.fetchall()
    print(rows)

    data = []
    for row in rows:
        row_data = {"id": row[0], "fname": row[1], "lname":row[2], "parentorguardian": row[3], "address": row[4], "contact": row[5], "presentclass": row[6], "classteacher": row[7]}   
        data.append(row_data)

        conn.close()
    return {"classes": data}






if __name__ == "__main__":
    app.run(debug=True)

 