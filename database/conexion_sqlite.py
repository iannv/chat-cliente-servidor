import sqlite3


def crear_tabla():
    conexion = None
    try:
        conexion = sqlite3.connect("database/chat.db")
        cursor = conexion.cursor()
        cursor.execute(
            """
            CREATE TABLE IF NOT EXISTS mensaje (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                contenido VARCHAR(255) NOT NULL,
                fecha_envio DATETIME,
                ip_cliente VARCHAR(15)
                )
                """
        )
        conexion.commit()
        print("Base de datos lista")

    except Exception as e:
        print(f"Error: {e}")

    finally:
        if conexion:
            conexion.close()


def guardar_mensaje(contenido, ip):
    conexion = None
    try:
        conexion = sqlite3.connect("database/chat.db")
        cursor = conexion.cursor()
        cursor.execute(
            """
                INSERT INTO mensaje (contenido, fecha_envio, ip_cliente) 
                VALUES (?, datetime('now'), ?)
                """,
            (contenido, ip),
        )
        conexion.commit()

    except Exception as e:
        print(f"Error: {e}")

    finally:
        if conexion:
            conexion.close()
