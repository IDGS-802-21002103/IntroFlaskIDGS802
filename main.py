"""Archivo principal de la aplicacion"""

from flask import Flask, request, render_template

import forms

app = Flask(__name__)

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
    
    if request.method == "POST":
        nombre = alumno_form.nombre.data
        apellido = alumno_form.apellido.data
        email = alumno_form.email.data
        
        print("Nombre: {}".format(nombre))
        print("Apellido: {}".format(apellido))
        print("Email: {}".format(email))
        
    return render_template("alumnos.html", form=alumno_form, nombre=nombre, apellido=apellido, email=email)


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
