import sqlite3
NOMBRE_DB="/home/felipe/Documentos/work/db/tutoriales.db"

def get_db():
    conexion = sqlite3.connect(NOMBRE_DB)
    return conexion

def crear_tablas():
    tablas = [
        """CREATE TABLE IF NOT EXISTS Creador(
                id_creador INTEGER PRIMARY KEY AUTOINCREMENT,
                str_nombre TEXT NOT NULL
            )""",
        """CREATE TABLE IF NOT EXISTS Tutorial(
                id_tutorial INTEGER PRIMARY KEY AUTOINCREMENT,
                str_tema TEXT NOT NULL,
				str_descripcion TEXT NOT NULL,
				str_titulo TEXT NOT NULL,
                visible BOOLEAN,
                fecha_creacion TEXT NOT NULL,
                creador_id INTEGER NOT NULL,
                FOREIGN KEY (creador_id) REFERENCES Creador (id_creador)
            )""",
        
    ]
    # ALTER TABLE Miembro ADD CONSTRAINT FK_MIEMBROPERSONA FOREIGN KEY ("k_tipoid", "k_id") REFERENCES Persona ("k_tipoid", "k_id");
    db = get_db()
    cursor = db.cursor()
    for tabla in tablas:
        cursor.execute(tabla)
