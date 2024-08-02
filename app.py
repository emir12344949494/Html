from flask import Flask, render_template, url_for, request

app = Flask(__name__, static_folder="static")

@app.route('/')
def iniciar():
    return render_template('futbol.html')

@app.route('/buscar')
def buscar():
    return render_template('buscarr.html')

@app.route('/desarrollador')
def contactos():
    return render_template('desarrolllador.html')

@app.route('/productos')
def productos():
    return render_template('products.html')

@app.route('/Estilos')
def Estilos():
    return render_template('styles.html')

@app.route('/person')
def index():
    return render_template('personn.html')


@app.route('/recuperar_psw', methods=['POST'])
def recuperar_psw():
    if request.method == 'POST':
       correo = request.form.get('email')
       nombre = request.form.get('nombre')
       contraseña = request.form.get('contraseña')
       opcion = request.form.get('opcion')
       print(nombre,       correo,    contraseña, opcion)

    return f"Se ha enviado la informacion al  correo electronico {nombre}    {correo}      {contraseña}    {opcion}"


if __name__ == '__main__':
    app.run(host='localhost', port=8090, debug=True)
