from db import mysql
from flask import Blueprint, flash, redirect, render_template, request, url_for

contacts = Blueprint('contacts', __name__, template_folder='app/templates')

@contacts.route('/')
def index():
    return render_template('login.html')

@contacts.route('/admin')
def admin():
    cur = mysql.connection.cursor()
    cur.execute('SELECT * FROM contacts')
    data = cur.fetchall()
    cur.close()
    return render_template('index.html', contacts=data)

@contacts.route('/login', methods=['POST'])
def login():
    username = request.form['username']
    password = request.form['password']

    # Validar los datos de inicio de sesión
    if username == 'a' and password == 'a':
        # Inicio de sesión exitoso, redireccionar a una página de inicio
        return redirect(url_for('contacts.admin'))
    else:
        # Inicio de sesión fallido, redireccionar al formulario de inicio de sesión

        return render_template('login.html', error_message='Credenciales incorrectas')
        
    
@contacts.route('/add_contact', methods=['POST'])
def add_contact():
    if request.method == 'POST':
        fullname = request.form['fullname']
        phone = request.form['phone']
        email = request.form['email']
        cc = request.form['cc']
        try:
            cur = mysql.connection.cursor()
            cur.execute(
                "INSERT INTO contacts (fullname, phone, email, cc) VALUES (%s,%s,%s,%s)", (fullname, phone, email, cc))
            mysql.connection.commit()
            flash('Agregado correctamente')
            return redirect(url_for('contacts.admin'))
        except Exception as e:
            flash(e.args[1])
            return redirect(url_for('contacts.admin'))


@contacts.route('/edit/<id>', methods=['POST', 'GET'])
def get_contact(id):
    cur = mysql.connection.cursor()
    cur.execute('SELECT * FROM contacts WHERE id = %s', (id))
    data = cur.fetchall()
    cur.close()
    print(data[0])
    return render_template('edit-contact.html', contact=data[0])


@contacts.route('/update/<id>', methods=['POST'])
def update_contact(id):
    if request.method == 'POST':
        fullname = request.form['fullname']
        phone = request.form['phone']
        email = request.form['email']
        cc = request.form['cc']
        cur = mysql.connection.cursor()
        cur.execute("""
            UPDATE contacts
            SET fullname = %s,
                email = %s,
                phone = %s,
                cc = %s
            WHERE id = %s
        """, (fullname, email, phone, cc, id))
        flash('Actualizado correctamente')
        mysql.connection.commit()
        return redirect(url_for('contacts.admin'))


@contacts.route('/delete/<string:id>', methods=['POST', 'GET'])
def delete_contact(id):
    cur = mysql.connection.cursor()
    cur.execute('DELETE FROM contacts WHERE id = {0}'.format(id))
    mysql.connection.commit()
    flash('Registro eliminado')
    return redirect(url_for('contacts.admin'))
