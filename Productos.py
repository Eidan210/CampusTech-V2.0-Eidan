import json
import os

ARCHIVO_PRODUCTOS = "Productos.json"
PRODUCTOS = []

def cargar_productos():
    global ARCHIVO_PRODUCTOS
    try:
        if os.path.exists(ARCHIVO_PRODUCTOS):
            with open(ARCHIVO_PRODUCTOS, "r") as archivo:
                try:
                    datos = json.load(archivo)
                    PRODUCTOS.clear()
                    PRODUCTOS.extend([
                        {
                            "Precio": g["Precio"],
                            "Stock": g["Stock"],
                            "Categoria": g["Categoria"],
                            "Producto": g["Producto"]
                        }
                        for g in datos
                    ])
                    print(f"Se cargaron {len(PRODUCTOS)} producto(s) desde '{ARCHIVO_PRODUCTOS}'.")
                except json.JSONDecodeError:
                    print(f"El archivo '{ARCHIVO_PRODUCTOS}' estaba corrupto. Se iniciará con lista vacía.")
                    PRODUCTOS.clear()
        else:
            PRODUCTOS.clear()
    except Exception as ex:
        print(f"Error inesperado al cargar los productos: {ex}")
        PRODUCTOS.clear()


def guardar_productos():
    try:
        datos = [
            {
                "Precio": g["Precio"],
                "Stock": g["Stock"],
                "Categoria": g["Categoria"],
                "Producto": g["Producto"],
            }
            for g in PRODUCTOS
        ]
        with open(ARCHIVO_PRODUCTOS, "w") as archivo:
            json.dump(datos, archivo, indent=4)
    except Exception as ex:
        print(f"Error inesperado al guardar los productos: {ex}")
