from flask import Flask, render_template, request, redirect, url_for
from flask_pymongo import PyMongo
from bson.objectid import ObjectId

app = Flask(__name__)

# MongoDB configuration
app.config["MONGO_URI"] = "mongodb+srv://22300040:Delta1500@dayrongc.b4fakiy.mongodb.net/BD1"
mongo = PyMongo(app)

@app.route('/')
def index():
    inventario = mongo.db.cantidad.find()
    registros = mongo.db.registro.find()
    return render_template('index.html', inventario=inventario, registros=registros)

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
    inventario = list(mongo.db.cantidad.find())
    return render_template('data.html', inventario=inventario)

@app.route('/add_item', methods=['GET', 'POST'])
def add_item():
    if request.method == 'POST':
        nombre = request.form['nombre']
        cantidad = request.form['cantidad']
        mongo.db.cantidad.insert_one({'nombre': nombre, 'cantidad': cantidad})
        return redirect(url_for('data'))
    return render_template('add_item.html')

@app.route('/delete_item/<item_id>')
def delete_item(item_id):
    mongo.db.cantidad.delete_one({'_id': ObjectId(item_id)})
    return redirect(url_for('data'))

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        producto = request.form['exacto']
        clave_empleado = request.form['username']
        contraseña = request.form['password']
        sucursal = request.form['sucursal']
        base_datos = request.form['data']
        mongo.db.registro.insert_one({
            'producto': producto,
            'clave_empleado': clave_empleado,
            'contraseña': contraseña,
            'sucursal': sucursal,
            'base_datos': base_datos
        })
        return redirect(url_for('inventario_route'))
    return render_template('register.html')

@app.route('/interior')
def visualize_data():
    inventario = list(mongo.db.cantidad.find())
    registros = list(mongo.db.registro.find())
    return render_template('interior.html', inventario=inventario, registros=registros)

@app.route('/editar_inventario/<id>', methods=['GET'])
def editar_inventario(id):
    item = mongo.db.cantidad.find_one({'_id': ObjectId(id)})
    return render_template('editar_inventario.html', item=item)

@app.route('/eliminar_inventario/<id>', methods=['POST'])
def eliminar_inventario(id):
    mongo.db.cantidad.delete_one({'_id': ObjectId(id)})
    return redirect(url_for('index'))

@app.route('/editar_registro/<id>', methods=['GET'])
def editar_registro(id):
    reg = mongo.db.registro.find_one({'_id': ObjectId(id)})
    return render_template('editar_registro.html', reg=reg)

@app.route('/eliminar_registro/<id>', methods=['POST'])
def eliminar_registro(id):
    mongo.db.registro.delete_one({'_id': ObjectId(id)})
    return redirect(url_for('index'))

@app.route('/anadir_registro', methods=['POST'])
def anadir_registro():
    producto = request.form.get('producto')
    clave_empleado = request.form.get('clave_empleado')
    contraseña = request.form.get('contraseña')
    sucursal = request.form.get('sucursal')
    base_datos = request.form.get('base_datos')
    
    mongo.db.registro.insert_one({
        'producto': producto,
        'clave_empleado': clave_empleado,
        'contraseña': contraseña,
        'sucursal': sucursal,
        'base_datos': base_datos
    })
    
    return redirect(url_for('index'))

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

