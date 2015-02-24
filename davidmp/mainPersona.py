# coding: utf-8
from include import app
from flask.templating import render_template
from flask import redirect, url_for, request
from ec.edu.itsae.dao import PersonaDAO




@app.route("/add", methods=['GET','POST'])
def formAdd():
    nombre=request.args.get("nombre")  #request.form['yourname']
    apellpaterno=request.args.get("apellpaterno")
    apellmaterno=request.args.get("apellmaterno")
    dni=request.args.get("dni")
    fnacimiento=request.args.get("fnacimiento")
    sexo=request.args.get("sexo")
    celular=request.args.get("celular")
    direccion=request.args.get("direccion")
    estado=int(request.args.get("estado"))
    PersonaDAO.PersonaDAO().insertarPersona(nombre, apellpaterno, apellmaterno,
                                             dni, fnacimiento, sexo, direccion, celular, estado)
    
    return redirect(url_for("index"))


@app.route("/validar")
def validar():
    usuario=request.args.get("username")    
    clave=request.args.get("password")
    
    x=PersonaDAO.PersonaDAO().login(usuario, clave)
    if len(x)==1:
        return redirect(url_for("index"))   
    else:
        return redirect(url_for("login"))     
    
     
@app.route("/autoB") 
def buscarPersonaAuto():
    dato=str(request.args.get('term'))
    resultado=PersonaDAO.PersonaDAO().buscarPersonaAuto(dato)
    print resultado
    return resultado

@app.route("/buscar", methods=['POST']) 
def buscarPersonaNombre():
    #dato=str(request.args.get('nombrebuscar'))
    dato=request.form['nombrebuscar'].encode('utf-8')
    
    resultado=PersonaDAO.PersonaDAO().buscarPersonaNombre(dato)
    #print resultado
    return render_template("index.html", dato=resultado)
    
    
    
    