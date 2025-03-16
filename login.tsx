import { NextResponse } from 'next/server';
import sqlite3 from 'sqlite3';
import { open } from 'sqlite';

import path from 'path';

async function openDb() {
  return open({
    filename: path.resolve(process.cwd(), 'database.db'), 
    driver: sqlite3.Database
  });
}


// API de Login
export async function POST(req: Request) {
    const { usuario, password } = await req.json();  
    console.log(`Usuario recibido: ${usuario}, Contraseña recibida: ${password}`); 
  
    const db = await openDb();
  
    const row = await db.get('SELECT * FROM Login WHERE usuario = ? AND password = ?', [usuario, password]);
  
    console.log("Resultado de la consulta:", row); 
  
    if (row) {
      return NextResponse.json({ message: 'Login exitoso' }, { status: 200 });
    } else {
      return NextResponse.json({ message: 'Usuario o contraseña incorrectos' }, { status: 401 });
    }
  }
  