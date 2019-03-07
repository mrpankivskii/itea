# pip install sqlalchemy

from sqlalchemy.ext.declarative import declarative_base

from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship, backref

Base = declarative_base()


class Department(Base):
    __tablename__ = 'departments'

    idDepartment = Column(Integer, primary_key=True)
    DepartmentCity = Column(String)
    CountOfWorkers = Column(Integer)

    def __repr__(self):
        return f'Id: {self.idDepartment} City: {self.DepartmentCity}'


class Client(Base):
    __tablename__ = 'clients'

    idClient = Column(Integer, primary_key=True)
    FirstName = Column(String)
    LastName = Column(String)
    Education = Column(String)
    Passport = Column(String)
    City = Column(String)
    Age = Column(Integer)

    department_id = Column(Integer,
                           ForeignKey('departments.idDepartment'))

    department = relationship('Department',
                              backref=backref('clients',
                                              order_by=idClient))

    def __repr__(self):
        return f'Name: {self.FirstName} Surname: {self.LastName}'


class Application(Base):
    __tablename__ = 'applications'

    idApplication = Column(Integer, primary_key=True)
    Sum = Column(Integer)
    CreditState = Column(String)
    Currency = Column(String)

    client_id = Column(Integer,
                      ForeignKey('clients.idClient'))

    client = relationship('Client',
                          backref=backref('applications',
                                          order_by=Sum))

    def __repr__(self):
        return f'Id: {self.idApplication} Sum: {self.Sum} ClientId: {self.client_id}'
