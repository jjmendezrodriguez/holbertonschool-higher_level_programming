#!/usr/bin/python3
import MySQLdb
import sys

if __name__ == "__main__":
    # Argumentos de línea de comandos
    mysql_username = sys.argv[1]
    mysql_password = sys.argv[2]
    database_name = sys.argv[3]

    # Conexión a la base de datos
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=mysql_username,
        passwd=mysql_password,
        db=database_name
    )

    # Crear un cursor para ejecutar las consultas
    cursor = db.cursor()

    # Ejecutar la consulta para listar todos los estados
    cursor.execute("SELECT * FROM states ORDER BY id ASC")

    # Obtener todos los resultados de la consulta
    states = cursor.fetchall()

    # Imprimir los resultados
    for state in states:
        print(state)

    # Cerrar el cursor y la conexión a la base de datos
    cursor.close()
    db.close()
