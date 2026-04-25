"""
Pipeline de datos usando JSONPlaceholder - Endpoint: /users
https://jsonplaceholder.typicode.com/users

Pasos del pipeline:
1. Obtener datos de usuarios desde la API.
2. Filtrar usuarios cuyo nombre de empresa contenga cierta letra.
3. Transformar los datos extrayendo campos relevantes.
4. Ordenar usuarios por nombre.
5. Mostrar el resultado final.
"""

import urllib.request
import json


BASE_URL = "https://jsonplaceholder.typicode.com"


def obtener_usuarios():
    """Paso 1: Ingesta - obtener lista de usuarios desde la API."""
    url = f"{BASE_URL}/users"
    with urllib.request.urlopen(url) as respuesta:
        datos = json.loads(respuesta.read().decode("utf-8"))
    print(f"[1] Usuarios obtenidos: {len(datos)}")
    return datos


def filtrar_usuarios_con_sitio_web(usuarios):
    """Paso 2: Filtrado - conservar solo usuarios que tienen sitio web registrado."""
    filtrados = [u for u in usuarios if u.get("website")]
    print(f"[2] Usuarios con sitio web: {len(filtrados)}")
    return filtrados


def transformar_usuarios(usuarios):
    """Paso 3: Transformación - extraer nombre, email, teléfono, empresa y ciudad."""
    transformados = [
        {
            "nombre": u["name"],
            "email": u["email"],
            "telefono": u["phone"],
            "empresa": u["company"]["name"],
            "ciudad": u["address"]["city"],
        }
        for u in usuarios
    ]
    print(f"[3] Usuarios transformados: {len(transformados)}")
    return transformados


def ordenar_por_nombre(usuarios):
    """Paso 4: Ordenamiento - ordenar la lista por nombre de forma ascendente."""
    ordenados = sorted(usuarios, key=lambda u: u["nombre"])
    print("[4] Usuarios ordenados por nombre.")
    return ordenados


def mostrar_resultados(usuarios):
    """Paso 5: Presentación - imprimir los datos finales."""
    print("\n--- Resultado final del pipeline ---")
    for u in usuarios:
        print(
            f"  Nombre   : {u['nombre']}\n"
            f"  Email    : {u['email']}\n"
            f"  Teléfono : {u['telefono']}\n"
            f"  Empresa  : {u['empresa']}\n"
            f"  Ciudad   : {u['ciudad']}\n"
        )


def ejecutar_pipeline():
    print("=== Iniciando pipeline de usuarios (JSONPlaceholder) ===\n")
    usuarios_crudos = obtener_usuarios()
    usuarios_filtrados = filtrar_usuarios_con_sitio_web(usuarios_crudos)
    usuarios_transformados = transformar_usuarios(usuarios_filtrados)
    usuarios_ordenados = ordenar_por_nombre(usuarios_transformados)
    mostrar_resultados(usuarios_ordenados)
    print("=== Pipeline completado ===")


if __name__ == "__main__":
    ejecutar_pipeline()
