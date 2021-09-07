from flask import Flask 
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI']='postgresql://postgres:password@localhost:5432/school_db'
app.config['SQLALCHEMY _TRACT_MODIFICATIONS'] = False

db=SQLAlchemy(app)
migrate = Migrate(app, db)

class Software_user(db.Model):
    user_id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), nullable=False)
    password = db.Column(db.String(15), nullable=False)

    def __repr__(self):
        return f"({self.username})"

class Section(db.Model):
    section_id = db.Column(db.Integer, primary_key=True)
    section = db.Column(db.String(25), nullable=False)

    def __repr__(self):
        return f"({self.section})"


class Department(db.Model):
    department_id = db.Column(db.Integer, primary_key=True)
    department = db.Column(db.String(25), nullable=False)
    staff = db.relationship('Staff', backref='Department', lazy=True)

    def __repr__(self):
        return f"({self.department})"

class All_classes(db.Model):
    class_id = db.Column(db.Integer, primary_key=True)
    classes = db.Column(db.String(25), nullable=False)
    staff = db.relationship('Staff', backref='All_class', lazy=True)
    student = db.relationship('Student', backref='All_class', lazy=True)

    def __repr__(self):
        return f"({self.classes})"

class Subject(db.Model):
    subject_id = db.Column(db.Integer, primary_key=True)
    subject = db.Column(db.String(25), nullable=False)
    staff = db.relationship('Staff', backref='Subject', lazy=True)

    def __repr__(self):
        return f"({self.subjects})"

class Staff(db.Model):
    staff_id = db.Column(db.Integer, primary_key=True)
    fname = db.Column(db.String(25), nullable=False)
    lname = db.Column(db.String(25), nullable=False)
    pnumber = db.Column(db.String(11), nullable=False)
    department = db.Column(db.Integer, db.ForeignKey(Department.department_id), nullable=False)
    formclass = db.Column(db.Integer, db.ForeignKey(All_classes.class_id), nullable=True)
    salary = db.Column(db.Integer, nullable=False)
    accountnumber = db.Column(db.Integer, nullable=False)
    bank = db.Column(db.String(50), nullable=False)
    dataofbirth = db.Column(db.String(50), nullable=False)
    subjectteaching = db.Column(db.Integer, db.ForeignKey(Subject.subject_id), nullable=True)
    student = db.ForeignKey('Student', backref='Staff', lazy=True)


    def __repr__(self):
        return f"({self.fname}, {self.lname})"

class Parent_guardian(db.Model):
    pg_id = db.Column(db.Integer, primary_key=True)
    fname = db.Column(db.String(25), nullable=False)
    lname = db.Column(db.String(25), nullable=False)
    pnumber = db.Column(db.Integer, nullable=False)
    email = db.Column(db.String(35), nullable=False)
    address = db.Column(db.String(50), nullable=False)
    student = db.relationship("Student", backref='Parent_guardian', lazy=True)

    def __repr__(self):
        return f"({self.fname}, {self.lname})"

class Student(db.Model):
    student_id = db.Column(db.Integer, primary_key=True)
    fname = db.Column(db.String(25), nullable=False)
    lname = db.Column(db.String(25), nullable=False)
    parentorguardian = db.Column(db.Integer, db.ForeignKey(Parent_guardian.pg_id), nullable=False)
    address = db.Column(db.Integer, db.ForeignKey(Parent_guardian.pg_id), nullable=False)
    contact = db.Column(db.Integer, db.ForeignKey(Parent_guardian.pg_id), nullable=False)
    presentclass = db.Column(db.Integer, db.ForeignKey(All_classes.class_id), nullable=False)
    classteacher = db.Column(db.Integer, db.ForeignKey(Staff.staff_id), nullable=False)

    def __repr__(self):
        return f"({self.fname} {self.lname})"


@app.route('/')
def index():
    return "Hello world"

if __name__ == "__main__":
    app.run(debug=True)
