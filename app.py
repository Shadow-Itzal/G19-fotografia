from flask import Flask, render_template, request, redirect
from controller_db import *

app = Flask(__name__)

# seccion inicio
@app.route("/")
def Inicio():
    title = "Inicio"
    return render_template("index.html", titulo=title)

# seccion galeria
@app.route("/galeria")
def galeria():
    title = "Galería"
    return render_template("galeria.html", titulo=title)

# seccion conoceme
@app.route("/conoceme")
def conoceme():
    title = "Conóceme"
    return render_template("conoceme.html", titulo=title)



# seccion contacto // cargar contacto
# INSERT 
# 1) cargar el form:
@app.route("/contacto")
def contacto():
    title = "Contacto"
    return render_template("contacto.html", titulo=title)

# 2) enviar los datos del form, por POST
@app.route("/contacto/guardar_nuevo_contacto", methods=['POST'])
def newContac_contacto():
    # print (request.form)

    nombre = request.form['nombre']
    email = request.form['email']
    telefono = request.form['telefono']
    fecha_evento = request.form['fecha_evento']
    mensaje = request.form['mensaje']

    cargar_contacto(nombre, email, telefono, fecha_evento, mensaje)
    return redirect("/contacto")


@app.route("/contacto-db")
def baseDatos():
    contactos = obtener_contactos()
    title = "Base de datos de clientes"
    return render_template("contacto-db.html", titulo=title, contactos=contactos) 


# update 

@app.route("/contacto-db/contacto-editar/<int:id>")
def edit_cont(id):
    title = "Editar contacto"
    cont_por_id = obtener_contactos_por_id(id)
    #print (cont_por_id)
    return render_template("contacto-editar.html", title=title, contactos = cont_por_id)

@app.route("/contacto-db/update_contacto", methods=['POST'])
def update_cont():
    id_edit = request.form['id']
    nombre_edit = request.form['nombre']
    email_edit = request.form['email']
    telefono_edit = request.form['telefono']
    fecha_evento_edit = request.form['fecha_evento']
    mensaje_edit = request.form['mensaje']
    actualizar_cont(nombre_edit, email_edit, telefono_edit, fecha_evento_edit, mensaje_edit, id_edit)
    return redirect("/contacto-db")


# borrar -> delete, 2 paso:

@app.route("/contacto-db/borrar_contacto/<int:id>")
def delete_cont(id):
    eliminar_cont(id)
    return redirect("/contacto-db")