# coding: utf-8
'''
Created on 17/2/2015

@author: PC06
'''
from include import app
from flask.templating import render_template
from ec.edu.itsae.dao import PersonaDAO

@app.route("/")
def login():
    return render_template("login.html")

@app.route("/persona")
def index():
    x=PersonaDAO.PersonaDAO().reportarPersona()
    print x
    return render_template("index.html", dato=x)