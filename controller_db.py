from db import conexionMySQL

# consultas -> CRUD

# read -> SELECT
def obtener_contactos():
    #conexion
    conexion = conexionMySQL()
    #consulta db

    with conexion.cursor() as cursor:
    # Read a record // leer registro
        query = "SELECT * FROM contactos"
        cursor.execute(query)

    #procesar los resultados -> fetch
        result = cursor.fetchall()

    #cerrar la conexion
        conexion.commit()
        conexion.close()
        return result

# create - insert
def cargar_contacto(nombre, email, telefono, fecha_evento, mensaje):
    conexion = conexionMySQL()
    with conexion.cursor() as cursor:
        query = "INSERT INTO contactos (nombre, email, telefono, fecha_evento, mensaje) VALUES (%s, %s, %s, %s, %s)"
        cursor.execute(query, (nombre, email, telefono, fecha_evento, mensaje))
        result = cursor
        conexion.commit()
        conexion.close()
        return result

# update -> 1)

def obtener_contactos_por_id(id):
    conexion = conexionMySQL()
    with conexion.cursor() as cursor:
        query = "SELECT * FROM contactos WHERE id = %s"
        cursor.execute(query, (id))
        cont = cursor.fetchone()
    conexion.commit()
    conexion.close()
    return cont

# update -> 2)

def actualizar_cont(nombre, email, telefono, fecha_evento, mensaje, id):
    conexion = conexionMySQL()
    with conexion.cursor() as cursor:
        cursor.execute("UPDATE contactos SET nombre = %s, email = %s, telefono = %s, fecha_evento = %s, mensaje = %s WHERE id = %s",(nombre, email, telefono, fecha_evento, mensaje, id))
        result = cursor
    conexion.commit()
    conexion.close()
    return result


# borrar -> delete, 1 paso:

def eliminar_cont(id):
    conexion = conexionMySQL()
    with conexion.cursor() as cursor:
        cursor.execute("DELETE FROM contactos WHERE id = %s", (id))
        result = cursor
    conexion.commit()
    conexion.close()
    return result


