from services.db import get_db


def obtener_tutoriales():
    db = get_db()
    cursor = db.cursor()
    query = "SELECT id_tutorial, str_tema, str_descripcion, str_titulo, visible, id_detalle FROM Tutorial"
    cursor.execute(query)
    return cursor.fetchall()


def obtener_tutorial_por_id(id):
    db = get_db()
    cursor = db.cursor()
    statement = "SELECT id_tutorial, str_tema, str_descripcion, str_titulo, visible, id_detalle FROM Tutorial WHERE id_tutorial = ?"
    cursor.execute(statement, [id])
    return cursor.fetchone()


def agregar_tutorial(tema, descripcion, titulo, visible, id_detalle):
    db = get_db()
    cursor = db.cursor()
    statement = "INSERT INTO Tutorial ( str_tema, str_descripcion, str_titulo, visible, id_detalle ) VALUES ( ?, ?, ?, ?, ? )"
    cursor.execute(statement, [tema, descripcion, titulo, visible, id_detalle])
    db.commit()
    return cursor.lastrowid


def actualizar_tutorial(id, tema, descripcion, titulo, visible, id_detalle):
    db = get_db()
    cursor = db.cursor()
    statement = "UPDATE Tutorial SET str_tema = ?, str_descripcion = ?, str_titulo = ?, visible = ?, id_detalle = ? WHERE id_tutorial = ?"
    cursor.execute(statement, [tema, descripcion, titulo, visible, id_detalle, id])
    db.commit()
    return True


def eliminar_tutorial_por_id(id):
    db = get_db()
    cursor = db.cursor()
    statement = "DELETE FROM Tutorial WHERE id = ?"
    cursor.execute(statement, [id])
    db.commit()
    return True
