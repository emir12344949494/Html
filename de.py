from flask import Flask, render_template, request, redirect, url_for
from pymongo import MongoClient

app = Flask(__name__)

def get_db():
    client = MongoClient('mongodb+srv://22300040:Delta1500@dayrongc.b4fakiy.mongodb.net/')
    db = client["BD1"]
    return db

def consult_all():
    db = get_db() 
    coleccion = db["usuarios"]
    doctos = list(coleccion.find({}))
    return doctos

@app.route('/')
def index():
    datos = consult_all()
    return render_template('index.html', datos=datos)

@app.route('/submit', methods=['POST'])
def submit():
    nombre = request.form.get('nombre')
    apellido = request.form.get('apellido')
    genero = request.form.get('genero')
    correo = request.form.get('correo')
    contraseña = request.form.get('contraseña')

    try:
        db = get_db()
        coleccion = db.usuarios
        coleccion.insert_one({
            'nombre': nombre,
            'apellido': apellido,
            'genero': genero,
            'correo': correo,
            'contraseña' : contraseña

        })
        return redirect(url_for('index'))
    except Exception as e:
        print("Error: tus datos no han sido registrados :(", e)
        return f"Hola {nombre}, {apellido}, tus datos no han sido registrados: {e}"

if __name__ == '__main__':
    app.run(debug=True, host='localhost', port=8090)
