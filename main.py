"""Archivo principal de la aplicacion"""

from flask import Flask, request, render_template
from flask_wtf.csrf import CSRFProtect
from flask import flash
from flask import g
import forms

app = Flask(__name__)
app.secret_key = 'mysecretkey'

@app.errorhandler(404)
def page_not_found(error):
        return render_template('error.html'), 404

@app.before_request
def before_request():
    g.prueba = 'Hola'
    print("ANTES DE LA RUTA")

@app.after_request
def after_request(response):
    print("DESPUES DE LA RUTA")
    return response

@app.route("/")
def index():
    """Funcion inicial de la aplicacion"""
    return render_template("index.html")

@app.route("/maestros")
def maestros():
    """Funcion para mostrar los maestros"""
    return render_template("maestros.html")

@app.route("/alumnos", methods=["GET", "POST"])
def alumnos():
    """Funcion para mostrar los alumnos"""
    alumno_form = forms.UserForm(request.form)
    nombre = ''
    apellido = ''
    email = ''
    valor = g.prueba
    print("EL valor es", valor)
    print(request.method)
    print("Formulario Valido",alumno_form.validate())
    print(alumno_form.errors)
    
    if request.method == "POST" and alumno_form.validate():
        nombre = alumno_form.nombre.data
        apellido = alumno_form.apellido.data
        email = alumno_form.email.data
        edad = alumno_form.edad.data
        flash("Alumno registrado correctamente")
        
        print("Nombre: {}".format(nombre))
        print("Apellido: {}".format(apellido))
        print("Email: {}".format(email))
        
        return render_template("alumnos.html", form=alumno_form, nombre=nombre, apellido=apellido, email=email, edad=edad)
    
    return render_template("alumnos.html", form=alumno_form, nombre='', apellido='', email='', edad='')

@app.route("/hello")
def hola_mundo():
    """Funcion inicial de la aplicacion"""
    return "<p>Hello, World!<p>"


@app.route("/hola")
def hola():
    """Funcion Hola de la aplicacion"""
    return "<p>Hola, Mundo!<p>"


@app.route("/saludo/<string:nombre>")
def saludo(nombre):
    """Funcion Saludo de la aplicacion"""
    return f"<p>Hola, {nombre}!<p>"


@app.route("/numero/<int:num>")
def numero(num):
    """Funcion Numero de la aplicacion"""
    return f"<p>El numero es {num}<p>"


@app.route("/user/<string:username>/<int:identificador>")
def user(username, identificador):
    """Funcion par Usuarios"""
    return f"ID: {identificador} NOMBRE: {username}"


@app.route("/suma/<int:num1>/<int:num2>")
def suma(num1, num2):
    """Funcion Suma de la aplicacion"""
    return f"La suma de {num1} + {num2} es {num1 + num2}"


@app.route("/multiplica", methods=["GET", "POST"])
def multiplica():
    """Funcion Multiplica de la aplicacion"""
    if request.method == "POST":
        numero_1 = request.form.get("numero1")
        numero_2 = request.form.get("numero2")
        resultado = int(numero_1) * int(numero_2)
        return f"<h1>El resultado es: {resultado}</h1>"

    else:
        return """
                <form action="/multiplica" method="POST">
                    <label>Numero 1</label>
                    <input type="text" name="numero1">
                    <label>Numero 2</label>
                    <input type="text" name="numero2">
                    <input type="submit" value="Multiplica">
                </form>
                 """

@app.route("/formulario1")
def formulario():
    """Funcion Formulario de la aplicacion"""
    return render_template("formulario_1.html")


@app.route("/resultado", methods=["POST", "GET"])
def multiplicacion():
    """Funcion Multiplicacion de la aplicacion"""
    if request.method == "POST":
        numero_1 = request.form.get("numero1")
        numero_2 = request.form.get("numero2")
        resultado = int(numero_1) * int(numero_2)
        return f"<h1>El resultado es: {resultado}</h1>"
    return "Error"

if __name__ == "__main__":
    app.run(debug=True)
