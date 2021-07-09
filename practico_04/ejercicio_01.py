"""Base de Datos SQL - Crear y Borrar Tablas"""

import sqlite3

def crear_tabla():
    """Implementar la funcion crear_tabla, que cree una tabla Persona con:
        - IdPersona: Int() (autoincremental)
        - Nombre: Char(30)
        - FechaNacimiento: Date()
        - DNI: Int()
        - Altura: Int()
    """
    db=sqlite3.connect(":memory:")

    cursor = db.cursor()
    cSQL = "CREATE TABLE IF NOT EXISTS persona(idpersona INTEGER AUTOINCREMENT, nombre TEXT(30), fechaNacimiento TEXT(10), dni INTEGER, altura INTEGER)"
    cursor.execute(cSQL)
    db.commit()
    db.close()


def borrar_tabla():
    """Implementar la funcion borrar_tabla, que borra la tabla creada 
    anteriormente."""
    db=sqlite3.connect(":memory:")

    cursor = db.cursor()
    cSQL = "DROP TABLE IF EXISTS persona"
    cursor.execute(cSQL)
    db.commit()
    db.close()


# NO MODIFICAR - INICIO
def reset_tabla(func):
    def func_wrapper():
        crear_tabla()
        func()
        borrar_tabla()
    return func_wrapper
# NO MODIFICAR - FIN
