from services.db import get_db


def obtener_tutoriales():
    db = get_db()
    cursor = db.cursor()
    query = "SELECT id_tutorial, str_tema, str_descripcion, str_titulo, visible, id_detalle FROM Tutorial"
    cursor.execute(query)
    return cursor.fetchall()
