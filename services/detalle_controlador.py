from services.db import get_db


def obtener_detalles():
    db = get_db()
    cursor = db.cursor()
    query = "SELECT id_detalle, fecha_creacion, str_nombre FROM Detalle"
    cursor.execute(query)
    return cursor.fetchall()


def obtener_detalle_por_id(id):
    db = get_db()
    cursor = db.cursor()
    statement = "SELECT id_detalle, fecha_creacion, str_nombre FROM Detalle WHERE id_detalle = ?"
    cursor.execute(statement, [id])
    return cursor.fetchone()


def agregar_detalle(nombre_autor):
    db = get_db()
    cursor = db.cursor()
    statement = "INSERT INTO Detalle (fecha_creacion, str_nombre ) VALUES (datetime('now', 'localtime'), ? )"
    cursor.execute(statement, [nombre_autor])
    db.commit()
    return cursor.lastrowid


def actualizar_detalle(id, nombre_autor):
    db = get_db()
    cursor = db.cursor()
    statement = "UPDATE Detalle SET str_nombre = ? WHERE id_detalle = ?"
    cursor.execute(statement, [nombre_autor, id])
    db.commit()
    return True


def eliminar_detalle_por_id(id):
    db = get_db()
    cursor = db.cursor()
    statement = "DELETE FROM Detalle WHERE id = ?"
    cursor.execute(statement, [id])
    db.commit()
    return True
