from flask import Flask, render_template, request, redirect, url_for
from pymongo import MongoClient
from bson.objectid import ObjectId

app = Flask(__name__, static_folder="static")

# MongoDB configuration
def get_db():
    client = MongoClient('mongodb+srv://22300040:Delta1500@dayrongc.b4fakiy.mongodb.net/')
    db = client["BD1"]
    return db

@app.route('/')
def principal():
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

@app.route('/folio')
def folio():
    return render_template('folio.html')

@app.route('/catalogo')
def catalogo():
    return render_template('catalogo.html')

@app.route('/buzon')
def buzon():
    return render_template('buzon.html')

@app.route('/person')
def person():
    return render_template('person.html')

@app.route('/inventario')
def inventario_route():
    return render_template('inventario.html')

@app.route('/vista')
def vista():
    return render_template('vista.html')

@app.route('/data')
def data():
    db = get_db()
    inventario = list(db.cantidad.find())
    return render_template('data.html', inventario=inventario)

@app.route('/add_item', methods=['GET', 'POST'])
def add_item():
    if request.method == 'POST':
        nombre = request.form['nombre']
        cantidad = request.form['cantidad']
        db = get_db()
        db.cantidad.insert_one({'nombre': nombre, 'cantidad': cantidad})
        return redirect(url_for('data'))
    return render_template('add_item.html')

@app.route('/delete_item/<item_id>')
def delete_item(item_id):
    db = get_db()
    db.cantidad.delete_one({'_id': ObjectId(item_id)})
    return redirect(url_for('data'))

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        producto = request.form['exacto']
        clave_empleado = request.form['username']
        contraseña = request.form['password']
        sucursal = request.form['sucursal']
        base_datos = request.form['data']
        db = get_db()
        db.registro.insert_one({
            'producto': producto,
            'clave_empleado': clave_empleado,
            'contraseña': contraseña,
            'sucursal': sucursal,
            'base_datos': base_datos
        })
        return redirect(url_for('inventario_route'))
    return render_template('register.html')

@app.route('/edit_record/<record_id>', methods=['GET', 'POST'])
def edit_record(record_id):
    db = get_db()
    record = db.registro.find_one({'_id': ObjectId(record_id)})
    if request.method == 'POST':
        producto = request.form['exacto']
        clave_empleado = request.form['username']
        contraseña = request.form['password']
        sucursal = request.form['sucursal']
        base_datos = request.form['data']
        db.registro.update_one(
            {'_id': ObjectId(record_id)},
            {'$set': {
                'producto': producto,
                'clave_empleado': clave_empleado,
                'contraseña': contraseña,
                'sucursal': sucursal,
                'base_datos': base_datos
            }}
        )
        return redirect(url_for('visualize_data'))
    return render_template('edit_record.html', record=record)

@app.route('/interior')
def visualize_data():
    db = get_db()
    inventario = list(db.cantidad.find())
    registros = list(db.registro.find())
    return render_template('interior.html', inventario=inventario, registros=registros)

if __name__ == '__main__':
    app.run(debug=True)












#Respuecuperar los datos 
#@app.route('/recuperar_psw', methods=['POST'])
#def recuperar_psw():
    #if request.method == 'POST':
        #correo = request.form.get('email')
        #nombre = request.form.get('nombre')
        #contraseña = request.form.get('contraseña')
        #opcion = request.form.get('opcion')
        #print(nombre, correo, contraseña, opcion)
    
    # Retornar
    #return f"Se ha enviado la informacion al correo electronico {nombre} {correo} {contraseña} {opcion}"

