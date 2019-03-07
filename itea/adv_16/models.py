# pip install sqlalchemy

from flask import Flask
from flask_login import LoginManager, UserMixin
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt

from sqlalchemy.orm import relationship, backref

app = Flask(__name__)
bcrypt = Bcrypt(app)

app = Flask(__name__)
app.secret_key = "super secret key"
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'

login_manager = LoginManager()
login_manager.init_app(app)

db = SQLAlchemy(app)


class Department(db.Model):
    idDepartment = db.Column(db.Integer, primary_key=True)
    DepartmentCity = db.Column(db.String)
    CountOfWorkers = db.Column(db.Integer)

    def __repr__(self):
        return f'Id: {self.idDepartment} City {self.DepartmentCity}'


class Client(db.Model):
    idClient = db.Column(db.Integer, primary_key=True)
    FirstName = db.Column(db.String)
    LastName = db.Column(db.String)
    Education = db.Column(db.String)
    Passport = db.Column(db.String)
    City = db.Column(db.String)
    Age = db.Column(db.Integer)

    department_id = db.Column(db.Integer,
                              db.ForeignKey('department.idDepartment'))

    department = relationship('Department',
                              backref=backref('clients',
                                              order_by=idClient))

    def __repr__(self):
        return f'Name: {self.FirstName} Surname {self.LastName}'


class Application(db.Model):
    idApplication = db.Column(db.Integer, primary_key=True)
    Sum = db.Column(db.Integer)
    CreditState = db.Column(db.String)
    Currency = db.Column(db.String)

    client_id = db.Column(db.Integer,
                          db.ForeignKey('client.idClient'))

    client = relationship('Client',
                          backref=backref('applications',
                                          order_by=Sum))

    def __repr__(self):
        return f'Id: {self.idApplication} Sum {self.Sum}' \
            f' ClientId {self.client_id}'


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    lastname = db.Column(db.String)
    email = db.Column(db.String, unique=True)
    password = db.Column(db.String)

    def __repr__(self):
        return f'Id: {self.id} Name {self.name}'


@login_manager.user_loader
def load_user(user_id):
    return User.query.filter_by(id=user_id).first()
