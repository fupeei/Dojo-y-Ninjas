from flask import render_template, request, redirect
from app_flask import app
from app_flask.modelos.dojos import Dojo
from app_flask.modelos.ninjas import Ninja

@app.route("/")
def dojos():
    lista_dojos = Dojo.seleccionar_todo()
    return render_template("dojos.html", lista_dojos = lista_dojos)

@app.route('/procesar/dojo', methods = ['POST'])
def procesar_dojo():
    nuevo_dojo = {
        'nombre_dojo' : request.form["nombre_dojo"]
    }
    id_nuevo_dojo = Dojo.agregar_uno(nuevo_dojo)
    return redirect ("/")

@app.route('/dojo/mostrar/<int:id>', methods=["GET"])
def mostrar_usuario(id):
    datos = {
        "id" : id
    }
    dojo = Dojo.seleccionar_uno(datos)
    lista_ninjas = Ninja.seleccionar_algunos(datos)
    return render_template('ver_dojo.html', dojo=dojo, lista_ninjas=lista_ninjas)