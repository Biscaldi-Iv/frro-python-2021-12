"""Base de Datos SQL - Creación de tablas auxiliares"""

from ejercicio_01 import borrar_tabla, crear_tabla
import sqlite3


def crear_tabla_peso():
    """Implementar la funcion crear_tabla_peso, que cree una tabla PersonaPeso con:
        - IdPersona: Int() (Clave Foranea Persona)
        - Fecha: Date()
        - Peso: Int()
    """
    db = sqlite3.connect("mybase.db")

    cursor = db.cursor()
    cSQL = "CREATE TABLE IF NOT EXISTS PersonaPeso (id INTEGER PRIMARY KEY, IdPersona INTEGER, fecha TEXT(10), peso INTEGER, FOREIGN KEY(IdPersona) REFERENCES persona(idpersona))"
    cursor.execute(cSQL)
    db.commit()
    cursor.close()
    db.close()


def borrar_tabla_peso():
    """Implementar la funcion borrar_tabla, que borra la tabla creada 
    anteriormente."""
    db = sqlite3.connect("mybase.db")

    cursor = db.cursor()
    cSQL = "DROP TABLE IF EXISTS PersonaPeso"
    cursor.execute(cSQL)
    cursor.close()
    db.commit()
    db.close()


# NO MODIFICAR - INICIO
def reset_tabla(func):
    def func_wrapper():
        crear_tabla()
        crear_tabla_peso()
        func()
        borrar_tabla_peso()
        borrar_tabla()
    return func_wrapper
# NO MODIFICAR - FIN
