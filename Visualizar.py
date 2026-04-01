from tabulate import tabulate
from Productos import PRODUCTOS

def reporte_categorias():
    while True:
        print("""
=============================================
            Visualizar Productos
=============================================""")
        print("Los Productos se mostraran ordenados por precio de menor a mayor\n")
        gastos_filtrados = []
        for p in PRODUCTOS:
            gastos_filtrados.append(p)
                
        n = len(gastos_filtrados)
        for i in range(n):
            for j in range(0, n - i - 1):
                if float(gastos_filtrados[j]["Precio"]) > float(gastos_filtrados[j + 1]["Precio"]):
                    temporal = gastos_filtrados[j]
                    gastos_filtrados[j] = gastos_filtrados[j + 1]
                    gastos_filtrados[j + 1] = temporal

        suma_total = 0
        for Producto in gastos_filtrados:
            suma_total += float(Producto["Precio"])

        if len(gastos_filtrados) == 0:
            print("No se encontraron categorias.")
            return
            
        lista_imprimir = []
        for gasto in gastos_filtrados:
            lista_imprimir.append([gasto["Precio"], gasto["Stock"], gasto["Categoria"], gasto["Producto"]])

        print(f"\nSe mostraran los datos en la terminal a continuacion: \n")
        tabla = tabulate(lista_imprimir, headers=["Precio", "Stock", "Categoria", "Producto"], tablefmt="fancy_grid", numalign="center", stralign="center")
        print(tabla)
        print(f"=============================================")
        print(f"       TOTAL Precios: ${suma_total}")
        print(f"=============================================\n")

        opcion = input("¿Desea Intentarlo denuevo S/N ? ").strip().capitalize()
        if opcion == "S":
            continue
        elif opcion == "N":
            return
        else:
            print("Opción no elegida o invalida")


