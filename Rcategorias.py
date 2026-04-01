from tabulate import tabulate
from Productos import PRODUCTOS

def Listar_Productos():
    print("""
=============================================
          Reporte de Categorías
=============================================
""")
    if len(PRODUCTOS) == 0:
        print("No hay categorias para mostrar (no hay productos registrados).\n")
        return

    
    categorias_unicas = set()
    for producto in PRODUCTOS:
        categorias_unicas.add(producto["Categoria"])

    
    lista_imprimir = []
    for categoria in categorias_unicas:
        lista_imprimir.append([categoria])

    tabla = tabulate(lista_imprimir, headers=["Categorías Presentes"], tablefmt="fancy_grid", numalign="center", stralign="center")
    print(tabla)
    print("\n")
