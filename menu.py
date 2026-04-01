from ProductosRegistro import registrar_Nuevo_Producto 
from Visualizar import reporte_categorias
from Rcategorias import Listar_Productos
from Productos import cargar_productos
from Productos import guardar_productos
def menu_principal():
    cargar_productos()
    while True:
        print("""
==========================================================
        Sistema Modular de Gestión "CampusTech v2.0"
==========================================================
Seleccione una opción:

1. Registrar Producto Tecnologico
2. Visualizar Productos
3. Reporte de Categorías
4. Salir
==========================================================""")
        try:
            opcion = int(input("Cual Opcion desea usar hoy: "))
            if opcion == 1:
                registrar_Nuevo_Producto()
            elif opcion == 2:
                reporte_categorias()
            elif opcion == 3:
                Listar_Productos()
            elif opcion == 4:
                Guardar = input ("¿Desea Guardar los archivos antes de salir S/N?: ").strip().capitalize()
                if Guardar == "S":
                    guardar_productos()
                    print("Archivos guardados exitosamente")
                    print("saliendo...")
                    break
                elif Guardar == "N":
                    print("¡La información no se guardo!")
                    print("saliendo...")
                    break
                else:
                    print("Opción no elegida o invalida")
                    continue
            else: 
                print("Opcion invalida, intentelo denuevo")
        except ValueError:
            print("Eliga una opcion Valida")

if __name__ == "__main__":
    menu_principal()

