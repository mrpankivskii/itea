import csv

from sqlalchemy import create_engine
from sqlalchemy import or_
from sqlalchemy.orm import sessionmaker

from models import Base, Department, Client, Application


engine = create_engine('sqlite:///database.db', echo=True)


def create_all_tables():
    Base.metadata.create_all(engine)


def set_up_database():
    Session = sessionmaker(bind=engine)
    session = Session()

    with open('department.csv') as source:
        reader = csv.DictReader(source)
        for d in reader:
            department = \
                Department(idDepartment=int(d['idDepartment']),
                           DepartmentCity=d['DepartmentCity'],
                           CountOfWorkers=int(d['CountOfWorkers']))
            session.add(department)

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
                       Age=int(c['Age']),
                       department_id=int(c['Department_idDepartment']))
            session.add(client)

    with open('application.csv') as source:
        reader = csv.DictReader(source)
        for a in reader:
            application = \
                Application(idApplication=int(a['idApplication']),
                       Sum=int(a['Sum']),
                       CreditState=a['CreditState'],
                       Currency=a['Currency'],
                       client_id=int(a['Client_idClient']))
            session.add(application)

    session.commit()


def custom_query():
    Session = sessionmaker(bind=engine)
    session = Session()
    print('1 All Clients')
    clients = session.query(Client).all()
    for client in clients:
        print(client)
    print('2 Lviv department')
    lviv_deps = session.query(Department).filter(Department.DepartmentCity =='Lviv').all()
    for dep in lviv_deps:
        print(dep)
    print('3 Clients with high education')
    high_clients = session.query(Client).filter(Client.Education == 'high').order_by(Client.LastName).all()
    for client in high_clients:
        print(client)
    print('4 last 5 application')
    five_application = session.query(Application).order_by(Application.Sum.desc()).limit(5).all()
    for application in five_application:
        print(application)
    print('5 LastName = iva or iv')
    last_iv_iva = session.query(Client).filter(or_(Client.LastName.like('%iv'), Client.LastName.like('%iva'))).all()
    for la in last_iv_iva:
        print(la)
    print('6 Clients from Kyiv')
    k_clients = session.query(Client).join(Department).filter(Department.DepartmentCity == 'Kyiv')
    for client in k_clients:
        print(client)
    print('7 Clients + passport')
    # pasport_client = session.query(Client).
    # for client in pasport_client:
    #     print(client)
    print('9 All clients count')
    print(session.query(Client).count())
    print(session.query(Client).join(Department).filter(Department.DepartmentCity=='Lviv').count())



if __name__ == '__main__':
    # create_all_tables()
    # set_up_database()
    custom_query()
