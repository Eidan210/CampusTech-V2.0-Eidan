# CampusTech v2.0 — inventario tecnológico modular

Sistema de gestión de inventario por consola, escrito en Python y repartido en módulos con una
responsabilidad cada uno. Persiste en JSON entre ejecuciones.

`Python` · `JSON`

---

## El problema

Llevar un inventario de productos tecnológicos a mano genera datos inconsistentes y sin
trazabilidad: no hay forma rápida de registrar, consultar ni agrupar el stock por categoría.

## La solución

Un menú por consola sobre cinco módulos separados por responsabilidad, con validación de la
entrada del usuario y confirmación explícita de guardado antes de cerrar.

```
==========================================================
        Sistema Modular de Gestion "CampusTech v2.0"
==========================================================
Seleccione una opcion:

1. Registrar Producto Tecnologico
2. Visualizar Productos
3. Reporte de Categorias
4. Salir
==========================================================
Cual Opcion desea usar hoy: _
```

## Estructura

```
menu.py                → punto de entrada y bucle del menú
Productos.py           → modelo y operaciones sobre el producto
ProductosRegistro.py   → alta de productos con validación
Visualizar.py          → listado en consola
Rcategorias.py         → reporte agrupado por categoría
Productos.json         → capa de persistencia
```

## Cómo ejecutarlo

Necesita Python 3. Sin dependencias externas:

```bash
git clone https://github.com/Eidan210/CampusTech-V2.0-Eidan.git
cd CampusTech-V2.0-Eidan
python menu.py
```

## Lo que demuestra

Programación modular en Python: separación de responsabilidades en archivos independientes,
validación de entrada en el borde del sistema y una capa de datos aislada del resto de la
aplicación, de modo que cambiar JSON por otra persistencia solo toca un archivo.

---

Parte de mi portafolio → **[eidan210.github.io/portafolio-junior](https://eidan210.github.io/portafolio-junior/)**
