from flask import Flask, render_template, request
from pymongo import MongoClient

app = Flask(__name__, static_folder="static")

# Configuración de la base de datos MongoDB
client = MongoClient('mongodb://localhost:27017/')
db = client['nombre_de_tu_base_de_datos']  # Cambia 'nombre_de_tu_base_de_datos' por el nombre de tu base de datos

# Redireccionar las rutas de HTML y Python
@app.route('/')
def iniciar():
    return render_template('principal.html')

@app.route('/buscar')
def buscar():
    return render_template('buscar.html')

@app.route('/marcas')
def marcas():
    return render_template('marcas.html')

@app.route('/productos')
def productos():
    return render_template('productos.html')

@app.route('/Folio')
def Folio():
    return render_template('Folio.html')

@app.route('/Estilos')
def Estilos():
    return render_template('Estilos.html')

@app.route('/Buzon')
def Buzon():
    return render_template('Buzon.html')

@app.route('/person')
def index():
    return render_template('person.html')

@app.route('/data')
def entrada():
    return render_template('data.html')

# Recuperar los datos
@app.route('/recuperar_psw', methods=['POST'])
def recuperar_psw():
    if request.method == 'POST':
        correo = request.form.get('email')
        nombre = request.form.get('nombre')
        contraseña = request.form.get('contraseña')
        opcion = request.form.get('opcion')
        print(nombre, correo, contraseña, opcion)
        # Guardar los datos en la base de datos MongoDB
        db.usuarios.insert_one({
            'nombre': nombre,
            'correo': correo,
            'contraseña': contraseña,
            'opcion': opcion
        })
    return f"Se ha enviado la información al correo electrónico {nombre} {correo} {contraseña} {opcion}"

if __name__ == '__main__':
    app.run(host='localhost', port=8090, debug=True)
