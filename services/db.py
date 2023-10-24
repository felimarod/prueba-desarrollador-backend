import sqlite3
NOMBRE_DB="db/tutoriales.db"

def get_db():
    conexion = sqlite3.connect(NOMBRE_DB)
    return conexion

def crear_tablas():
    tablas = [
        """CREATE TABLE IF NOT EXISTS Detalle (
                id_detalle INTEGER PRIMARY KEY,
                fecha_creacion TEXT NOT NULL,
                str_nombre TEXT NOT NULL
            )""",
        """CREATE TABLE IF NOT EXISTS Tutorial(
                id_tutorial INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
                str_tema TEXT NOT NULL,
				str_descripcion TEXT NOT NULL,
				str_titulo TEXT NOT NULL,
                visible BOOLEAN,
                id_detalle INTEGER NOT NULL,
                FOREIGN KEY (id_detalle) REFERENCES Detalle (id_detalle)
            )""",
        
    ]
    db = get_db()
    cursor = db.cursor()
    for tabla in tablas:
        cursor.execute(tabla)
