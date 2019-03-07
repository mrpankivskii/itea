import csv

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from models import Base, Department, Client, Application

engine = create_engine('sqlite:///datebase.db', echo=True)


def create_all_tables():
    Base.metadata.create_all(engine)


def set_up_database():
    Session = sessionmaker(bind=engine)
    session = Session()
    with open('department.csv') as source:
        reader = csv.DictReader(source)
        for department in reader:
            # import ipdb; ipdb.set_trace()
            dep = \
                Department(idDepartment=int(department['idDepartment']),
                           DepartmentCity=department['DepartmentCity'],
                           CountOfWorkers=int(department['CountOfWorkers']),
                           )
            session.add(dep)

    with open('client.csv') as source:
        reader = csv.DictReader(source)
        for c in reader:
            client = \
                Client(idClient=int(c['idClient']),
                       FirstName=c['FirstName'],
                       LastName=c['LastName'],
                       Education=c['Education'],
                       Passport=c['Passport'],
                       City=c['City'],
                       Age=c['Age'],
                       department_id=c[int('Department_idDepartment')]),
            session.add(client)

    with open('application.csv') as source:
        reader = csv.DictReader(source)
        for a in reader:
            application = \
                Application(idApplication=int(a['idApplication']),
                            Sum=int(a['Sum']),
                            CreditState=a['CreditState'],
                            Currency=a['Currency'],
                            client_id=int(a["Client_idClient"]))

            session.add(application)


if __name__ == '__main__':
    create_all_tables()
    set_up_database()
