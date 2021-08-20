import sqlite3 as sqlite
import os

ruta=os.path.dirname(__file__)
db=ruta+"\\database"

def Conexion():
    conexion=sqlite.connect(os.path.join(db, "menus.db"))
    return conexion

def AgregarMenu(menu, acompanamiento, ensalada):
    conexion=Conexion()
    datos=(menu, acompanamiento, ensalada)
    consulta="INSERT INTO menu (plato, acompanamiento, ensalada) VALUES (?, ?, ?)"
    cursor=conexion.cursor()
    cursor.execute(consulta, datos)
    conexion.commit()
    conexion.close()

def BuscarIndividual(menu):
    dato=(menu, )
    conexion=Conexion()
    consulta="SELECT * FROM menu WHERE plato=?"
    cursor=conexion.cursor()
    cursor.execute(consulta, dato)
    resultado=cursor.fetchone()
    conexion.close()
    return resultado

def BuscarTodos():
    conexion=Conexion()
    cursor=conexion.cursor()
    cursor.execute("SELECT * from menu ORDER BY idmenu ASC")
    listado=cursor.fetchall()
    conexion.close()
    return listado

def BorrarMenu(menu):
    conexion=Conexion()
    consulta="DELETE FROM menu WHERE plato=?"
    cursor=conexion.cursor()
    cursor.execute(consulta, menu)
    conexion.commit()
    conexion.close()

def ModificarMenu(menu, acompanamiento, ensalada, menu_antiguo):
    conexion=Conexion()
    datos=(menu, acompanamiento, ensalada, menu_antiguo)
    consulta="UPDATE menu SET plato=?, acompanamiento=?, ensalada=? WHERE plato=?"
    cursor=conexion.cursor()
    cursor.execute(consulta, datos)
    conexion.commit()
    conexion.close()



"""
conexion=sqlite.connect(os.path.join(db, "menus.db"))
cursor=conexion.cursor()
cursor.execute("CREATE TABLE menu (idmenu INTEGER PRIMARY KEY AUTOINCREMENT, plato TEXT, acompanamiento INTEGER, ensalada INTEGER)")
cursor.execute("CREATE TABLE semana (id INTEGER PRIMARY KEY AUTOINCREMENT, plato TEXT, ensalada TEXT, fecha DATETIME)")
conexion.commit()
conexion.close()
"""
