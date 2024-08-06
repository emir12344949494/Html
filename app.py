from flask import Flask, render_template, request, redirect, url_for, jsonify, flash
from pymongo import MongoClient
from bson.objectid import ObjectId
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__, static_folder="static")
app.secret_key = 'supersecretkey'  # Cambia esto a una clave secreta segura

# MongoDB configuration
def get_db():
    client = MongoClient('mongodb+srv://22300040:Delta1500@dayrongc.b4fakiy.mongodb.net/BD1')
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

@app.route('/de')
def de():
    return render_template('de.html')


@app.route('/add_item', methods=['GET', 'POST'])
def add_item():
    if request.method == 'POST':
        nombre = request.form.get('nombre', '')
        cantidad = request.form.get('cantidad', '')
        if not nombre or not cantidad:
            flash('Nombre y cantidad son requeridos', 'error')
            return render_template('add_item.html')
        db = get_db()
        db.cantidad.insert_one({'nombre': nombre, 'cantidad': cantidad})
        return redirect(url_for('register'))
    return render_template('add_item.html')

@app.route('/delete_item/<item_id>')
def delete_item(item_id):
    db = get_db()
    db.cantidad.delete_one({'_id': ObjectId(item_id)})
    return redirect(url_for('data'))

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        producto = request.form.get('exacto', '')
        clave_empleado = request.form.get('username', '')
        contraseña = request.form.get('password', '')
        sucursal = request.form.get('sucursal', '')
        base_datos = request.form.get('data', '')
        if not producto or not clave_empleado or not contraseña or not sucursal or not base_datos:
            flash('Todos los campos son requeridos', 'error')
            return render_template('register.html')
        hashed_password = generate_password_hash(contraseña)
        db = get_db()
        db.registro.insert_one({
            'producto': producto,
            'clave_empleado': clave_empleado,
            'contraseña': hashed_password,
            'sucursal': sucursal,
            'base_datos': base_datos
        })
        flash('Registro exitoso', 'success')
        return redirect(url_for('inventario_route'))
    return render_template('register.html')

@app.route('/edit_record/<record_id>', methods=['GET', 'POST'])
def edit_record(record_id):
    db = get_db()
    record = db.registro.find_one({'_id': ObjectId(record_id)})
    if request.method == 'POST':
        producto = request.form.get('exacto', '')
        clave_empleado = request.form.get('username', '')
        contraseña = request.form.get('password', '')
        sucursal = request.form.get('sucursal', '')
        base_datos = request.form.get('data', '')
        if not producto or not clave_empleado or not contraseña or not sucursal or not base_datos:
            flash('Todos los campos son requeridos', 'error')
            return render_template('edit_record.html', record=record)
        hashed_password = generate_password_hash(contraseña)
        db.registro.update_one(
            {'_id': ObjectId(record_id)},
            {'$set': {
                'producto': producto,
                'clave_empleado': clave_empleado,
                'contraseña': hashed_password,
                'sucursal': sucursal,
                'base_datos': base_datos
            }}
        )
        flash('Registro actualizado exitosamente', 'success')
        return redirect(url_for('visualize_data'))
    return render_template('edit_record.html', record=record)

@app.route('/interior')
def visualize_data():
    db = get_db()
    inventario = list(db.cantidad.find())
    registros = list(db.registro.find())
    return render_template('interior.html', inventario=inventario, registros=registros)

@app.route('/update', methods=['POST'])
def update():
    db = get_db()
    data = request.get_json()
    item_id = data.get('id', '')
    nombre = data.get('nombre', '')
    cantidad = data.get('cantidad', '')
    if not item_id or not nombre or not cantidad:
        return jsonify({'success': False, 'message': 'ID, nombre y cantidad son requeridos'})
    
    result = db.cantidad.update_one(
        {'_id': ObjectId(item_id)},
        {'$set': {'nombre': nombre, 'cantidad': cantidad}}
    )
    
    if result.modified_count > 0:
        return jsonify({'success': True})
    else:
        return jsonify({'success': False, 'message': 'No se pudo actualizar el ítem'})

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        clave_empleado = request.form.get('username', '')
        contraseña = request.form.get('password', '')
        db = get_db()
        user = db.registro.find_one({'clave_empleado': clave_empleado})
        if user and check_password_hash(user['contraseña'], contraseña):
            flash('Inicio de sesión exitoso', 'success')
            return redirect(url_for('inventario_route'))
        else:
            flash('Usuario o contraseña incorrectos', 'error')
    return render_template('login.html')

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

