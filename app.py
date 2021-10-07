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
        user = data[0]['username']
        passcode = data[0]['password']

        print(user)
        print(passcode)
        query = "INSERT INTO SOFTWARE_USER(username, password) VALUES(%s, %s)"
        bind = (user, passcode,)
        cursor.execute( query, bind )
        conn.commit()
        conn.close()

@app.route('/create_department', methods=["POST"]) 
def create_department():
    conn = getconnection('school_db', 'postgres', 'password', '127.0.0.1', '5432')
    cursor = conn.cursor()

    if request.method=="POST":
        data = json.loads(request.data,strict=False)
        department = data[0]['department']
 
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
        firstname = data[0]['fname']
        lastname = data[0]['lname']
        pg = data[0]['parentorguardian']
        paddress = data[0]['address']
        pcontact = data[0]['contact']
        pclass = data[0]['presentclass']
        classteacher = data[0]['classteacher']
        
        print(firstname)
        print(lastname)
        print(pg)
        print(paddress)
        print(pcontact)
        print(pclass)
        print(classteacher)
        query = "INSERT INTO STUDENT(FNAME, LNAME, PARENTORGUARDIAN, ADDRESS, CONTACT, PRESENTCLASS, CLASSTEACHER) VALUES( %s, %s, %s, %s, %s, %s, %s)"
        bind = (firstname, lastname, phonenumber, Paddress, pcontact, pclass, classteacher)
        cursor.execute( query, bind )
        # conn.commit()
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

        query = "INSERT INTO PARENT_GUARDIAN(FNAME, LNAME, PNUMBER, EMAIL, ADDRESS) VALUES( %s, %s, %s, %s, %s)"
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
        subject = data[0]['subject']
 
        print(subject)

        query = "INSERT INTO SUBJECT(SUBJECT) VALUES( %s)"
        bind = (subject,)
        cursor.execute( query, bind )
        conn.commit()
        conn.close()

    return "done"


@app.route('/create_staf', methods=["POST"]) 
def create_staff():
    conn = getconnection('school_db', 'postgres', 'password', '127.0.0.1', '5432')
    cursor = conn.cursor()

    if request.method=="POST":
        data = json.loads(request.data,strict=False)
        firstname = data[0]['fname']
        lastname = data[0]['lname']
        pnumber = data[0]['pnumber']
        department = data[0]['department']
        formclass = data[0]['formclass']
        account = data[0]['accountnumber']
        salary = data[0]['salary']
        bank = data[0]['bank']
        dob = data[0]['dateofbirth']
        subject = data[0]['subjectteaching']
        email = data[0]['email']
        address = data[0]['address']
        
        print(firstname)
        print(lastname)
        print(phonenumber)
        print(email)
        print(address)

        query = "INSERT INTO STAFF(FNAME, LNAME, PNUMBER, DEPARTMENT, FORMCLASS, ACCOUNT, SALARY, BANK, DATEOFBRITH, SUBJECTTEACHING, EMAIL, ADDRESS) VALUES( %s, %s, %s, %s, %s)"
        bind = (firstname, lastname, phonenumber, email, address)
        cursor.execute( query, bind )
        conn.commit()
        conn.close()

    return "done"




if __name__ == "__main__":
    app.run(debug=True)

 