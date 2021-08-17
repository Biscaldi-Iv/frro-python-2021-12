"""Base de Datos SQL - Alta"""

import datetime
import sqlite3
from ejercicio_01 import reset_tabla


def agregar_persona(nombre, nacimiento, dni, altura):
    """Implementar la funcion agregar_persona, que inserte un registro en la 
    tabla Persona y devuelva los datos ingresados el id del nuevo registro."""
    db = sqlite3.connect("mybase.db")
    cursor = db.cursor()
    cmd = """INSERT INTO persona (idpersona, nombre, fechaNacimiento, dni, altura) 
         VALUES (null, ? , ? , ? , ? )  """
    cursor.execute(cmd, (nombre, nacimiento, dni, altura))
    db.commit()
    consulta = """SELECT idpersona, nombre, fechaNacimiento, dni, altura FROM persona WHERE nombre= ?"""
    cursor.execute(consulta, [nombre])
    result = cursor.fetchone()
    cursor.close()
    db.close()
    _id, _nom, _nac, _dni, _altura = result[0], result[1], result[2], result[3], result[4]
    return _id  # , _nom, _nac, _dni, _altura


# NO MODIFICAR - INICIO
@reset_tabla
def pruebas():
    id_juan = agregar_persona(
        'juan perez', datetime.datetime(1988, 5, 15), 32165498, 180)
    id_marcela = agregar_persona(
        'marcela gonzalez', datetime.datetime(1980, 1, 25), 12164492, 195)
    assert id_juan > 0
    assert id_marcela > id_juan


if __name__ == '__main__':
    pruebas()
# NO MODIFICAR - FIN
