from db import mysql
from flask import Blueprint, flash, redirect, render_template, request, url_for

contacts = Blueprint('contacts', __name__, template_folder='app/templates')

@contacts.route('/')
def index():
    return render_template('login.html')

@contacts.route('/admin_alumnos')
def admin_alumnos():
    cur = mysql.connection.cursor()
    cur.execute('SELECT * FROM contacts')
    data = cur.fetchall()
    cur.close()
    return render_template('indexAlumnos.html', contacts=data)

@contacts.route('/admin_cursos')
def admin_cursos():
    cur = mysql.connection.cursor()
    cur.execute('SELECT * FROM cursos')
    data = cur.fetchall()
    cur.close()
    return render_template('indexCursos.html', cursos=data)

@contacts.route('/alumno_cursos')
def alumno_cursos():
    cur = mysql.connection.cursor()
    cur.execute('SELECT * FROM cursos')
    data = cur.fetchall()
    cur.close()
    return render_template('vistaAlumnoCursos.html', cursos=data)

@contacts.route('/admin_profesores')
def admin_profesores():
    cur = mysql.connection.cursor()
    cur.execute('SELECT * FROM profesores')
    data = cur.fetchall()
    cur.close()
    return render_template('indexProfesores.html', profesores=data)

@contacts.route('/alumno_profesores')
def alumno_profesores():
    cur = mysql.connection.cursor()
    cur.execute('SELECT * FROM profesores')
    data = cur.fetchall()
    cur.close()
    return render_template('vistaAlumnoProfesores.html', profesores=data)

@contacts.route('/login', methods=['POST'])
def login():
    username = request.form['username']
    password = request.form['password']

    # Validar los datos de inicio de sesión
    if username == 'juantutriadmin123' and password == 'juantutriadmin123':
        # Inicio de sesión exitoso, redireccionar a una página de inicio
        return redirect(url_for('contacts.admin_alumnos'))
    else:
        if username == 'juantutrialumno123' and password == 'juantutrialumno123':
            # Inicio de sesión exitoso, redireccionar a una página de inicio
            return redirect(url_for('contacts.alumno_cursos'))
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
            return redirect(url_for('contacts.admin_alumnos'))
        except Exception as e:
            flash(e.args[1])
            return redirect(url_for('contacts.admin_alumnos'))
        
@contacts.route('/add_cursos', methods=['POST'])
def add_cursos():
    if request.method == 'POST':
        codigo = request.form['codigo']
        materia = request.form['materia']
        creditos = request.form['creditos']
        try:
            cur = mysql.connection.cursor()
            cur.execute(
                "INSERT INTO cursos (codigo, materia, creditos) VALUES (%s,%s,%s)", (codigo, materia, creditos))
            mysql.connection.commit()
            flash('Agregado correctamente')
            return redirect(url_for('contacts.admin_cursos'))
        except Exception as e:
            flash(e.args[1])
            return redirect(url_for('contacts.admin_cursos'))

@contacts.route('/add_profesores', methods=['POST'])
def add_profesores():
    if request.method == 'POST':
        nombre = request.form['nombre']
        salario = request.form['salario']
        cc = request.form['cc']
        try:
            cur = mysql.connection.cursor()
            cur.execute(
                "INSERT INTO profesores (nombre, salario, cc) VALUES (%s,%s,%s)", (nombre, salario, cc))
            mysql.connection.commit()
            flash('Agregado correctamente')
            return redirect(url_for('contacts.admin_profesores'))
        except Exception as e:
            flash(e.args[1])
            return redirect(url_for('contacts.admin_profesores'))

@contacts.route('/edit_alumnos/<id>', methods=['POST', 'GET'])
def get_contact(id):
    cur = mysql.connection.cursor()
    cur.execute('SELECT * FROM contacts WHERE id = %s', [id])
    data = cur.fetchall()
    cur.close()
    print(data[0])
    return render_template('editAlumnos.html', contact=data[0])

@contacts.route('/edit_cursos/<id>', methods=['POST', 'GET'])
def get_curso(id):
    cur = mysql.connection.cursor()
    cur.execute('SELECT * FROM cursos WHERE id = %s', [id])
    data = cur.fetchall()
    cur.close()
    print(data[0])
    return render_template('editCursos.html', curso=data[0])

@contacts.route('/edit_profesores/<id>', methods=['POST', 'GET'])
def get_profesor(id):
    cur = mysql.connection.cursor()
    cur.execute('SELECT * FROM profesores WHERE id = %s', [id])
    data = cur.fetchall()
    cur.close()
    print(data[0])
    return render_template('editProfesores.html', profesor=data[0])

@contacts.route('/update_alumnos/<id>', methods=['POST'])
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
        return redirect(url_for('contacts.admin_alumnos'))

@contacts.route('/update_cursos/<id>', methods=['POST'])
def update_curso(id):
    if request.method == 'POST':
        codigo = request.form['codigo']
        materia = request.form['materia']
        creditos = request.form['creditos']
        cur = mysql.connection.cursor()
        cur.execute("""
            UPDATE cursos
            SET codigo = %s,
                materia = %s,
                creditos = %s
            WHERE id = %s
        """, (codigo, materia, creditos, id))
        flash('Actualizado correctamente')
        mysql.connection.commit()
        return redirect(url_for('contacts.admin_cursos'))
    
@contacts.route('/update_profesores/<id>', methods=['POST'])
def update_profesor(id):
    if request.method == 'POST':
        nombre = request.form['nombre']
        salario = request.form['salario']
        cc = request.form['cc']
        cur = mysql.connection.cursor()
        cur.execute("""
            UPDATE profesores
            SET nombre = %s,
                salario = %s,
                cc = %s
            WHERE id = %s
        """, (nombre, salario, cc, id))
        flash('Actualizado correctamente')
        mysql.connection.commit()
        return redirect(url_for('contacts.admin_profesores'))


@contacts.route('/delete_alumnos/<string:id>', methods=['POST', 'GET'])
def delete_contact(id):
    cur = mysql.connection.cursor()
    cur.execute('DELETE FROM contacts WHERE id = {0}'.format(id))
    mysql.connection.commit()
    flash('Registro eliminado')
    return redirect(url_for('contacts.admin_alumnos'))

@contacts.route('/delete_cursos/<string:id>', methods=['POST', 'GET'])
def delete_curso(id):
    cur = mysql.connection.cursor()
    cur.execute('DELETE FROM cursos WHERE id = {0}'.format(id))
    mysql.connection.commit()
    flash('Registro eliminado')
    return redirect(url_for('contacts.admin_cursos'))

@contacts.route('/delete_profesores/<string:id>', methods=['POST', 'GET'])
def delete_profesor(id):
    cur = mysql.connection.cursor()
    cur.execute('DELETE FROM profesores WHERE id = {0}'.format(id))
    mysql.connection.commit()
    flash('Registro eliminado')
    return redirect(url_for('contacts.admin_profesores'))
