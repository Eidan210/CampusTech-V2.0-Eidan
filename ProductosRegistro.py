
from Productos import PRODUCTOS

def registrar_Nuevo_Producto():
    print("""
=============================================
    Registrar Nuevo Producto Tecnologico
=============================================
Ingrese la información del Producto:
""")
    while True:
        try:
            Precio = float(input("Precio: "))
            if Precio <= 0:
                print("Precio invalido, intente denuevo")
                continue
            Stock = int(input("¿Cuanto Stock Del Producto?: ").strip())
            if Stock <= 0:
                print("El Stock es 0 o Negativo Intentelo Denuevo.")
                continue
            categoria = str(input("Categoria (ej. Audifonos,Computadores,Relojes Inteligentes etc): ").strip().capitalize())
            Producto = str(input("¿Que Producto Añadiste?: ").strip().capitalize())

            if not Precio or not categoria:
                raise ValueError("El Precio y categoria son obligatorios, Intente otra vez.")
            else:
                guardar_o_no = input("Ingrese 'S' para guardar en un diccionario o 'N' para cancelar. ").strip().capitalize()

                if guardar_o_no == "S":
                    producto_dict = {
                        "Precio": Precio,
                        "Stock": Stock,
                        "Categoria": categoria,
                        "Producto": Producto
                    }
                    PRODUCTOS.append(producto_dict)
                    print("\n¡El Registro de Productos se realizo con exito!")
                    print("=============================================")
                    volver = input("\n¿Desea volver al menu? S/N: ").strip().upper()
                    if volver == "S":
                        return
                    elif volver == "N":
                        continue
                    else:
                        raise ValueError("Opción no elegida o invalida")

                elif guardar_o_no == "N":
                    print("¡La información no se guardo!")
                    print("=============================================")
                    intento = (input("\n¿Desea Intentarlo Denuevo? S/N: ")).strip().upper()
                    if intento == "S":
                        continue
                    elif intento == "N":
                        print("=============================================")
                        volver = input("\n¿Desea volver al menu? S/N: ").strip().upper()
                        if volver == "S":
                            return
                        elif volver == "N":
                            continue
                        else:
                            raise ValueError("Opción no elegida o invalida")

                else:
                    print("No se escribio nada, eliga la opcion S/N")
                    continue
        except ValueError as ve:
            print(f"Error de Registro: {ve}")