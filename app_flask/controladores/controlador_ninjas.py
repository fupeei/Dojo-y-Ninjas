from flask import render_template, request, redirect
from app_flask import app
from app_flask.modelos.ninjas import Ninja
from app_flask.modelos.dojos import Dojo

@app.route('/ninja/nuevo')         
def nuevo_ninja():
    lista_dojos = Dojo.seleccionar_todo()
    return render_template('nuevo_ninja.html', lista_dojos=lista_dojos)

@app.route('/procesar/ninja/nuevo', methods = ['POST'])
def procesar_ninja():
    nuevo_ninja = {
        'first_name' : request.form["nombre"],
        'last_name': request.form["apellido"],
        'age': request.form["edad"],
        'dojo_id': request.form["id_dojo"]
    }
    id_nuevo_usuario=Ninja.agregar_uno(nuevo_ninja)
    return redirect (f'/dojo/mostrar/{request.form["id_dojo"]}')

#(f'/usuarios/mostrar/{id_nuevo_usuario}')