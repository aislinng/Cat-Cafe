from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import sqlite3
from typing import List
from fastapi.responses import StreamingResponse
import io
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Servidor funcionando"}


# Configuración de CORS: actualiza según el puerto en el que se ejecute tu Next.js
origins = ["http://localhost:3000"]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

def get_db_connection():
    conn = sqlite3.connect("database.db")
    conn.row_factory = sqlite3.Row  
    return conn

class Usuario(BaseModel):
    usuario: str
    password: str

class Gato(BaseModel):
    id: int
    nombre: str
    descripcion: str

class Plato(BaseModel):
    id: int
    nombre_plato: str
    descripcion: str = ""
    precio: float

@app.post("/validar_usuario")
async def validar_usuario(usuario: Usuario):
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute("SELECT * FROM Login WHERE usuario = ? AND password = ?", (usuario.usuario, usuario.password))
    user = cur.fetchone()
    conn.close()
    if user:
        return {"message": "Usuario validado con éxito"}
    else:
        raise HTTPException(status_code=401, detail="Usuario o contraseña incorrectos")

@app.get("/menu", response_model=List[Plato])
async def leer_menu():
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute("SELECT rowid as id, alimento, precio FROM Menu")
    menu_items = cur.fetchall()
    conn.close()
    platos = [
        Plato(id=row["id"], nombre_plato=row["alimento"], descripcion="", precio=row["precio"])
        for row in menu_items
    ]
    return platos

@app.get("/gatos", response_model=List[Gato])
async def leer_gatos():
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute("SELECT rowid as id, nombre, descripcion FROM Gatos")
    gatos = cur.fetchall()
    conn.close()
    gatos_list = [
        Gato(id=row["id"], nombre=row["nombre"], descripcion=row["descripcion"])
        for row in gatos
    ]
    return gatos_list

@app.get("/gato/{gato_id}/imagen")
async def obtener_imagen(gato_id: int):
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute("SELECT imagen FROM Gatos WHERE rowid = ?", (gato_id,))
    imagen = cur.fetchone()
    conn.close()
    if imagen and imagen["imagen"]:
        return StreamingResponse(io.BytesIO(imagen["imagen"]), media_type="image/jpeg")
    else:
        raise HTTPException(status_code=404, detail="Imagen no encontrada")

@app.get("/textos")
async def obtener_textos():
    textos = {
        "home_title": "CatCafe",
        "home_description": (
            "Meow Cat Café es más que una cafetería, es un refugio para quienes buscan "
            "buena compañía felina y sabores reconfortantes. Rodeado de arte y detalles "
            "únicos, es el lugar ideal para disfrutar de un café especial y relajarte en "
            "un ambiente acogedor."
        )
    }
    return textos

@app.get("/")
def read_root():
    return {"message": "¡Servidor FastAPI en funcionamiento correctamente!"}
