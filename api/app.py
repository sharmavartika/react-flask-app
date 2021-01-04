from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.debug = True
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///employee.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

class Employee(db.Model):
    __tablename__ = 'employee'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(200))
    email = db.Column(db.String(200), unique=True)

    def __init__ (self, name, email):
        self.name = name
        self.email = email


@app.route('/')
def index():
    return "Hello developers!"

@app.route('/employees', methods=['POST'])
def add_employee():
    data = request.get_json()
    employee = Employee(data['name'], data['email'])
    db.session.add(employee)
    db.session.commit()
    return "Employee Added!!"

@app.route('/employees/<id>', methods=['GET'])
def get_employee(id):
    emp =  Employee.query.filter_by(id=id).first()
    return jsonify(
        {'id':emp.id,'name': emp.name, 'email': emp.email}
    )

@app.route('/employees/<id>', methods=['PUT'])
def update_employee(id):
    data = request.get_json()
    employee = Employee.query.filter_by(id=id).first()
    employee.name = data['name']
    employee.email = data['email']
    db.session.commit()
    emp = Employee.query.filter_by(id=id).first()
    return jsonify(
        {'id':emp.id,'name': emp.name, 'email': emp.email}
    )

@app.route('/employees/<id>', methods=['DELETE'])
def delete_employees(id):
    Employee.query.filter_by(id=id).delete()
    return "Employee Deleted!!"

@app.route('/employees', methods=['GET'])
def get_all_employees():
    employees =  Employee.query.all()
    return jsonify([
        {'id':emp.id,'name': emp.name, 'email': emp.email}
        for emp in employees
    ])


if __name__ == '__main__':
    app.run()