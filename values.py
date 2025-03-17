import sqlite3

try:
    with sqlite3.connect("database.db") as conn:

        cur = conn.cursor()
        # insert values for login
        cur.execute("""INSERT INTO Login(usuario,password)
                    VALUES(?,?);""",
                    ("lolo", "password"))
        conn.commit()
        # insert values for menu
        cur.execute("""INSERT INTO Menu(alimento,precio)
                    VALUES(?,?);""",
                    ("matcha", "90"))
        conn.commit()
        cur.execute("""INSERT INTO Menu(alimento,precio)
                    VALUES(?,?);""",
                    ("espresso", "80"))
        conn.commit()
        cur.execute("""INSERT INTO Menu(alimento,precio)
                    VALUES(?,?);""",
                    ("latte", "78"))
        conn.commit()
        # insert values for gatos
        cur.execute("""INSERT INTO Gatos(nombre,imagen, descripcion)
                    VALUES(?,?,?);""",
                    ("latte", "cafe.jpg","78"))
        
        
        conn.commit()
        def convertir_a_blob(ruta_imagen):
            with open(ruta_imagen, 'rb') as file:
                return file.read()
            # Insertar imagen en la base de dato
        nombre = "latio"
        imagen_blob = convertir_a_blob("cafe.jpg")  # Reemplaza con la ruta de tu imagen
        descripcion = "78"
        cur.execute("INSERT INTO Gatos (nombre, imagen, descripcion) VALUES (?, ?, ?)", 
            (nombre, imagen_blob, descripcion))
        conn.commit()
        
        


    pass 
except sqlite3.OperationalError as e:
    print("Failed to open database:",e)