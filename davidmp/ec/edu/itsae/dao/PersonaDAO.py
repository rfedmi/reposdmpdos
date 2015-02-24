# coding: utf-8
'''
Created on 17/2/2015

@author: PC06
'''
from ec.edu.itsae.conn import DBcon
import json

class PersonaDAO(DBcon.DBcon):
    '''
    classdocs
    '''


    def __init__(self):
        '''
        Constructor
        '''
    pass

    def reportarPersona(self):
        #con=self.connexion().connect().cursor()
        con=self.connexion().cursor()
        sql="select * from personas"
        con.execute(sql)
        row=con.fetchall()
        return row
        
    def insertarPersona(self, nombre, aparteno, amaterno, dni, fnacimiento, sexo,direccion, celular, esatado):
        con=self.connexion()
        sql="""insert into personas(nombre, apell_paterno, apell_materno, 
                dni, fecha_nacimiento, sexo, direccion, celular, estado) 
                values('%s','%s', '%s', '%s','%s', '%s', '%s', '%s', %i) 
                 """ % (nombre, aparteno, amaterno, dni, fnacimiento, sexo,direccion, celular, esatado )
        print sql
        with con:
            cursor=con.cursor()
            cursor.execute(sql)
        
        
        
    def login(self, usuario, clave):
        con=self.connexion().cursor()
        sql="select * from trabajador where usuario='%s' and clave='%s' " % (usuario, clave)
        con.execute(sql)
        row=con.fetchall()
        print row
        return row
    
    def buscarPersonaAuto(self, dato):
        con=self.connexion().cursor()
        sql=""" select CONCAT(nombre,' ', apell_paterno,' ', apell_materno) as value, 
                idpersona as id from personas 
                 where  upper(CONCAT(nombre,' ', apell_paterno,' ', apell_materno)) like upper('%s') """ % ("%"+dato+"%")
        con.execute(sql)
        reporte=con.fetchall()
        columna=('value', 'id')
        lista=[]
        for row in reporte:
            lista.append(dict(zip(columna, row)))        
        return json.dumps(lista, indent=2)
            
    def buscarPersonaNombre(self, dato):
        con=self.connexion().cursor()
        sql=""" select * from personas 
            where  upper(CONCAT(nombre,' ', apell_paterno,' ', apell_materno)) 
                  like upper('%s') """ % ("%"+dato+"%")
        con.execute(sql)
        reporte=con.fetchall()                    
        return reporte            
            
            
            
            
        
        
        
        
        