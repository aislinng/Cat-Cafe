// app/login/page.tsx
'use client'

import { useState, FormEvent } from "react";
import { useRouter } from 'next/navigation';

export default function Login() {
  const [usuario, setUsername] = useState<string>("");
  const [password, setPassword] = useState<string>("");
  const router = useRouter();

  const handleLogin = async (e: FormEvent) => {
    e.preventDefault();
    try {
      const response = await fetch('http://localhost:8000/validar_usuario', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ usuario, password })
      });
      const data = await response.json();
      console.log("Respuesta del servidor:", data);
      if (response.ok) {
        router.push("/main");
      } else {
        alert(data.detail || "Usuario o contraseña incorrectos");
      }
    } catch (error) {
      console.error("Error en la conexión:", error);
      alert("Error al conectar con el servidor");
    }
  };

  return (
    <div className="flex flex-col items-center justify-center min-h-screen p-8">
      <h1 className="text-3xl font-bold mb-8">Iniciar sesión</h1>
      <form className="flex flex-col gap-4" onSubmit={handleLogin}>
        <input
          type="text"
          placeholder="Usuario"
          value={usuario}
          onChange={(e) => setUsername(e.target.value)}
          className="border border-gray-300 p-2 rounded"
        />
        <input
          type="password"
          placeholder="Contraseña"
          value={password}
          onChange={(e) => setPassword(e.target.value)}
          className="border border-gray-300 p-2 rounded"
        />
        <button
          type="submit"
          className="mt-4 p-2 bg-blue-500 text-white rounded"
        >
          Iniciar sesión
        </button>
      </form>
    </div>
  );
}
