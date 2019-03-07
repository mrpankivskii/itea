import csv
import unittest
import os

from bs4 import BeautifulSoup

from models import Department, Client, Application, User, db
from app import app


class TestFlaskApp(unittest.TestCase):

    @classmethod
    def setUpClass(cls):

        cls.departments = []
        cls.clients = []
        cls.applications = []
        app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'

        cls.client = app.test_client()
        cls.client.testing = True
        db.create_all()

        with open(f'{os.path.dirname(os.path.realpath(__file__))}/department.csv') as source:
            reader = csv.DictReader(source)
            for d in reader:
                department = \
                    Department(idDepartment=int(d['idDepartment']),
                               DepartmentCity=d['DepartmentCity'],
                               CountOfWorkers=int(d['CountOfWorkers']))
                db.session.add(department)
                cls.departments.append(department)

        with open(f'{os.path.dirname(os.path.realpath(__file__))}/client.csv') as source:
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
                db.session.add(client)
                cls.clients.append(client)

        with open(f'{os.path.dirname(os.path.realpath(__file__))}/application.csv') as source:
            reader = csv.DictReader(source)
            for a in reader:
                application = \
                    Application(idApplication=int(a['idApplication']),
                                Sum=int(a['Sum']),
                                CreditState=a['CreditState'],
                                Currency=a['Currency'],
                                client_id=int(a['Client_idClient']))
                db.session.add(application)
                cls.applications.append(application)

        db.session.commit()

    @classmethod
    def tearDownClass(cls):
        os.remove(f'{os.getcwd()}/test.db')


    def test_departments(self):

        response = self.client.get('/departments')

        soup = BeautifulSoup(response.data, 'html.parser')

        self.assertEqual(response.status_code, 200)

        table = soup.find(id="dataTable")
        deps = table.find_all('tbody')[0].find_all('tr')
        self.assertEqual(len(deps), len(self.departments))

        self.assertEqual(
            int(deps[0].find_all('td')[0].text),
            self.departments[0].idDepartment
        )
