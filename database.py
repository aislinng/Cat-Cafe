import sqlite3

conn = sqlite3.connect('database.db')
cursor = conn.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS Menu (
    alimento TEXT,
    precio INT
)
''')

cursor.execute('''
CREATE TABLE IF NOT EXISTS Gatos (
    nombre TEXT,
    imagen BLOB,
    descripcion TEXT
)
''')

cursor.execute('''
CREATE TABLE IF NOT EXISTS Login (
    usuario TEXT,
    password TEXT
)
''')

conn.commit()

conn.close()

print("Base de datos creada exitosamente.")