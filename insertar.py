import sqlite3

def leer_imagen_como_blob(ruta_imagen):
    with open(ruta_imagen, "rb") as file:  
        return file.read()
    
try:
    with sqlite3.connect("database.db") as conn:

        cur = conn.cursor()
        # insert values for login
        cur.execute("""INSERT INTO Login(usuario,password)
                    VALUES(?,?);""",
                    ("lolo", "password"))
        conn.commit()
        cur.execute("""INSERT INTO Login(usuario,password)
                    VALUES(?,?);""",
                    ("usuario1", "contra1234"))
        conn.commit()
        
        # insert values for menu
        Menu = {
    "lunes": [
        ("Café Gatuno Especial", "$55"),
        ("Macarons Felinos de Frambuesa", "$45"),
        ("Galletas Purrfectos", "$35"),
        ("Pastel de Atún con Queso", "$60"),
        ("Latte con Leche de Almendra para Gatos", "$50")
    ],
    "martes": [
        ("Café Miauccino", "$50"),
        ("Cupcakes con Sabor a Pescado", "$40"),
        ("Galletas Catnip", "$30"),
        ("Pastelito de Pollo en Miniatura", "$70"),
        ("Frappuccino Miau", "$60")
    ],
    "miercoles": [
        ("Café con Gato Cacao", "$55"),
        ("Pastel de Pequeñas Ratitas", "$65"),
        ("Churros Miau", "$45"),
        ("Donas Ratoncitas", "$50"),
        ("Té de Hierba Gatera", "$40")
    ],
    "jueves": [
        ("Café con Leche de Gata", "$50"),
        ("Croissants con Sabor a Atún", "$45"),
        ("Macarrones Gatunos", "$55"),
        ("Pastel de Pollo Gato Gourmet", "$75"),
        ("Frappé de Pescado Fresco", "$65")
    ],
    "viernes": [
        ("Café Espresso con Sombra de Gato", "$55"),
        ("Cupcakes de Camarones", "$50"),
        ("Galletas para Gatos Mágicos", "$40"),
        ("Pastel de Gambas en Miniatura", "$80"),
        ("Café Frappé Miau Especial", "$70")
    ],
    "sabado": [
        ("Café Latte 'Gato Padrino'", "$60"),
        ("Mini Pasteles de Pescado y Calabaza", "$55"),
        ("Galletas Felinas de Menta", "$35"),
        ("Pastel de Queso con Ratón", "$75"),
        ("Frappé de Gata Tropical", "$65")
    ],
    "domingo": [
        ("Café con Sabor a Ratón", "$50"),
        ("Galletas en Forma de Patita de Gato", "$40"),
        ("Pastel de Gato Feliz (Chocolate Blanco)", "$70"),
        ("Macarons de Sabor a Pescado", "$45"),
        ("Frappuccino Gato del Día", "$60")
    ]
}
        for day, items in Menu.items():
            for alimento, precio in items:
                cur.execute("""INSERT INTO Menu(alimento, precio) VALUES(?, ?);""", (alimento, precio))
        conn.commit()
        
        # insert values for gatos
        cur.execute("""INSERT INTO Gatos(nombre, descripcion, imagen)
               VALUES(?, ?, ?);""", 
               ("Don Bigotes", "Un gordito simpático que siempre trae algo dulce y da consejos sabios.", leer_imagen_como_blob("media/gato1.webp")))
        conn.commit()

        cur.execute("""INSERT INTO Gatos(nombre, descripcion, imagen)
                    VALUES(?, ?, ?);""", 
                    ("Mimi la Artista", "Gata bohemia, creativa y soñadora. Ama la música jazz y decora las paredes de la cafetería con sus propios cuadros.", leer_imagen_como_blob("media/gato2.webp")))
        conn.commit()

        cur.execute("""INSERT INTO Gatos(nombre, descripcion, imagen)
                    VALUES(?, ?, ?);""", 
                    ("Capitán Ronroneo", "Gato aventurero con parche y pañuelo, siempre contando historias de sus viajes imaginarios.", leer_imagen_como_blob("media/gato3.webp")))
        conn.commit()


    pass

except sqlite3.OperationalError as e:
    print("Failed to open database:",e)
