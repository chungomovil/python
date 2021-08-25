import sqlite3 as sqlite
from sqlite3 import Error
import os

ruta=os.path.dirname(__file__)
db=ruta+"\\database"

def Conexion():
    conexion=sqlite.connect(os.path.join(db, "menus.db"))
    return conexion

def AgregarMenu(menu, categoria, acompanamiento, ensalada):
    conexion=Conexion()
    datos=(menu, categoria, acompanamiento, ensalada)
    consulta="INSERT INTO menu (plato, categoria, acompanamiento, ensalada) VALUES (?, ?, ?, ?)"
    cursor=conexion.cursor()
    cursor.execute(consulta, datos)
    conexion.commit()
    conexion.close()

def BuscarIndividual(menu):
    conexion=Conexion()
    dato=(menu, )
    consulta="SELECT * FROM menu WHERE plato=?"
    cursor=conexion.cursor()
    cursor.execute(consulta, dato)
    resultado=cursor.fetchone()
    conexion.close()
    return resultado

def BuscarTodos():
    conexion=Conexion()
    cursor=conexion.cursor()
    cursor.execute("SELECT * from menu ORDER BY plato ASC")
    listado=cursor.fetchall()
    conexion.close()
    return listado

def BorrarMenu(menu):
    dato=(menu, )
    conexion=Conexion()
    consulta="DELETE FROM menu WHERE plato=?"
    cursor=conexion.cursor()
    cursor.execute(consulta, dato)
    conexion.commit()
    conexion.close()


def ModificarMenu(menu, categoria, acompanamiento, ensalada, menu_antiguo):
    conexion=Conexion()
    datos=(menu, categoria, acompanamiento, ensalada, menu_antiguo)
    consulta="UPDATE menu SET plato=?, categoria=?, acompanamiento=?, ensalada=? WHERE plato=?"
    cursor=conexion.cursor()
    cursor.execute(consulta, datos)
    conexion.commit()
    conexion.close()

def AgregarMenuDia(idmenu, plato, dia, fecha):
    conexion=Conexion()
    datos=(idmenu, plato, dia, fecha)
    consulta="INSERT INTO semana (idmenu, plato, dia, fecha) VALUES (?, ?, ? ,?)"
    cursor=conexion.cursor()
    cursor.execute(consulta, datos)
    conexion.commit()
    conexion.close()

def ListaMenuDia():
    conexion=Conexion()
    cursor=conexion.cursor()
    cursor.execute("SELECT * FROM semana WHERE fecha=(SELECT MAX(fecha) FROM semana) ORDER BY id ASC")
    listado_recientes=cursor.fetchall()
    cursor.execute("SELECT * FROM semana WHERE fecha=(SELECT MIN(fecha) FROM semana) ORDER BY id ASC")
    listado_antiguos=cursor.fetchall()
    conexion.close()
    return (listado_recientes, listado_antiguos)

def BorrarMenuDia(fecha):
    fecha=(fecha, )
    conexion=Conexion()
    cursor=conexion.cursor()
    cursor.execute("DELETE FROM semana WHERE fecha=?", (fecha))
    conexion.commit()
    conexion.close()



"""
conexion=sqlite.connect(os.path.join(db, "menus.db"))
cursor=conexion.cursor()
cursor.execute("CREATE TABLE menu (idmenu INTEGER PRIMARY KEY AUTOINCREMENT, plato TEXT, categoria TEXT, acompanamiento TEXT, ensalada TEXT)")
cursor.execute("CREATE TABLE semana (id INTEGER PRIMARY KEY AUTOINCREMENT, idmenu INTEGER, dia TEXT, fecha DATETIME, FOREIGN KEY(idmenu) REFERENCES menu(idmenu))")
conexion.commit()
conexion.close()
"""
