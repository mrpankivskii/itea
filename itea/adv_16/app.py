from flask import render_template, redirect, request, url_for, flash
from flask_login import login_user, logout_user, login_required

from models import (
    app, db, bcrypt,
    Department, User, Client, Application
)


@app.route('/')
def index_page():
    return render_template('index.html')


@app.route('/departments')
def departments():
    deps = Department.query.all()
    return render_template('departments.html',
                           departments=deps)


@app.route('/clients')
def clients():
    clients = Client.query.all()
    return render_template('clients.html',
                           clients=clients)


@app.route('/applications')
def applications():
    applications = Application.query.all()
    return render_template('applications.html',
                           applications=applications)


@app.route('/department/<int:department_id>/clients')
def department_clients(department_id):
    clients = Client.query.filter_by(department_id=department_id).all()
    return render_template('clients.html',
                           clients=clients)


@app.route('/add-department', methods=['GET', 'POST'])
@login_required
def add_department():
    if request.method == 'POST':
        department_city = request.form['department_city']
        count_of_workers = request.form['count_of_workers']
        department = \
            Department(DepartmentCity=department_city,
                       CountOfWorkers=count_of_workers)
        db.session.add(department)
        db.session.commit()
        return redirect(url_for('departments'))
    return render_template('add_department.html')


@app.route('/department/<int:department_id>/add-client', methods=['GET', 'POST'])
@login_required
def add_client(department_id):
    if request.method == 'POST':
        department = Department.query.filter_by(idDepartment=department_id).first()
        if department:
            first_name = request.form['first_name']
            last_name = request.form['last_name']
            education = request.form['education']
            passport = request.form['passport']
            city = request.form['city']
            age = request.form['age']
            client = Client(FirstName=first_name,
                            LastName=last_name,
                            Education=education,
                            Passport=passport,
                            City=city,
                            Age=age,
                            department_id=department_id)

            db.session.add(client)
            db.session.commit()
            return redirect(url_for('department_clients', department_id=department_id))
        return redirect(url_for('departments'))
    return render_template('add_client.html')


@app.route('/department/<int:department_id>/client/<int:client_id>/add_application', methods=['GET', 'POST'])
@login_required
def add_application(department_id, client_id):
    if request.method == 'POST':
        department = Department.query.filter_by(idDepartment=department_id).first()
        if department:
            client = Client.query.filter_by(idClient=client_id).first()
            if client:
                summ = request.form['summ']
                creditstate = request.form['creditstate']
                currency = request.form['currency']
                application = Application(Sum=summ,
                                          CreditState=creditstate,
                                          Currency=currency,
                                          client_id=client_id)
                db.session.add(application)
                db.session.commit()
                return redirect(url_for('applications'))
            return redirect(url_for('department_clients', department_id=department_id))
        return redirect(url_for('departments'))
    return render_template('add_application.html')


@app.route('/remove_application/<int:application_id>')
@login_required
def remove_application(application_id):
    appl = Application.query.all()
    for application in appl:
        if application.idApplication == application_id:
            db.session.delete(application)
            db.session.commit()
            return redirect(url_for('applications'))


@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        name = request.form['name']
        lastname = request.form['lastname']
        email = request.form['email']
        password = request.form['password']
        confirm_password = request.form['confirm_password']
        if password != confirm_password:
            return render_template('register.html')
        pw_hash = bcrypt.generate_password_hash(password)
        user = \
            User(name=name, lastname=lastname, email=email, password=pw_hash)
        db.session.add(user)
        db.session.commit()
        return redirect(url_for('login'))
    return render_template('register.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        user = User.query.filter_by(email=email).first()
        if user:
            if bcrypt.check_password_hash(user.password, password):
                login_user(user)
                flash('Logged in successfully.')
            return redirect(url_for('departments'))
        flash('Credentials dont match')
        return redirect(url_for('register'))
    return render_template('login.html')


@login_required
@app.route('/logout', methods=['GET'])
def logout():
    logout_user()
    return redirect(url_for('login'))


if __name__ == '__main__':
    db.create_all()
    app.run(host='0.0.0.0', port=5000, debug=True)
