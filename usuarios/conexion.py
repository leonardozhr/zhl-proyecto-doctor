#conexion a la base de datos
import mysql.connector

def conectar():
    database = mysql.connector.connect(
        host = "localhost",
        user = "root",
        passwd = "",
        database = "zhl_proyectoDoc",
        port = 3306
    )
    cursor = database.cursor(buffered = True)
    return [database, cursor]
