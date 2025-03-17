import sqlite3
from flask import Flask, request, jsonify, send_from_directory, send_file
import io

from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Habilita CORS para todas las rutas




# Función para conectar a la base de datos
def conectar_bd():
    return sqlite3.connect("database.db")

# 1. Validar usuario
@app.route('/validar_usuario', methods=['POST'])
def validar_usuario():
    data = request.json
    usuario = data.get("usuario")
    password = data.get("password")

    with conectar_bd() as conn:
        cur = conn.cursor()
        cur.execute("SELECT * FROM Login WHERE usuario=? AND password=?", (usuario, password))
        user = cur.fetchone()

    if user:
        return jsonify({"mensaje": "Inicio de sesión exitoso"})
    else:
        return jsonify({"mensaje": "Usuario o contrasena incorrectos"}), 401


@app.route('/menu', methods=['GET'])
def leer_menu():
    # Obtener el valor de 'data' desde la URL (parámetro de consulta)
    data = request.args.get('data', default=1, type=int)
    print(f"Valor de data recibido: {data}")

    if data == 1:
        inicio = 0
    elif data == 2:
        inicio = 5
    elif data == 3:
        inicio = 10
    elif data == 4:
        inicio = 15
    elif data == 5:
        inicio = 20
    elif data == 6:
        inicio = 25
    else:
        return jsonify({"error": "El parámetro 'data' solo puede ser un valor entre 1 y 6."}), 400
    
    print(f"Valor de inicio: {inicio}")

    # Conectar a la base de datos y obtener los alimentos dentro del rango
    with conectar_bd() as conn:
        cur = conn.cursor()
        cur.execute("SELECT alimento, precio FROM Menu LIMIT 5 OFFSET ?", (inicio,))
        menu = [{"alimento": row[0], "precio": row[1]} for row in cur.fetchall()]

    return jsonify(menu)



@app.route('/gatos/<nombre_gato>', methods=['GET'])
def leer_gato(nombre_gato):
    with conectar_bd() as conn:
        cur = conn.cursor()
        cur.execute("SELECT descripcion FROM Gatos WHERE nombre=?", (nombre_gato,))
        resultado = cur.fetchone()

    if resultado:
        gato = {
            "descripcion": resultado[0]
        }
        return jsonify(gato)
    else:
        return jsonify({"error": "Gato no encontrado"}), 404
    

@app.route('/obtener_imagen/<nombre_gato>', methods=['GET'])
def obtener_imagen(nombre_gato):
    with conectar_bd() as conn:
        cur = conn.cursor()
        cur.execute("SELECT imagen FROM Gatos WHERE nombre=?", (nombre_gato,))
        resultado = cur.fetchone()

    if resultado:
        imagen_binaria = resultado[0]  # Datos en BLOB
        return send_file(io.BytesIO(imagen_binaria), mimetype='image/jpeg')
    else:
        return jsonify({"error": "Imagen no encontrada"}), 404 
    
    
textos = {
     "saludo": "Hola", "despedida": "Adiós",
}

@app.route('/textos', methods=['GET'])
def obtener_textos():
    return jsonify(textos)



if __name__ == '__main__':
    app.run(debug=True)
