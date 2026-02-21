# Importa tus módulos aquí
from data.biblioteca import libros, categorias
from utils.operaciones import (
    mostrar_disponibles,
    buscar_por_paginas,
    contar_libros,
    promedio_paginas,
    agregar_categoria
)

continuar = "s"

while continuar == "s":
    print("\n=== BIBLIOTECA ===")
    print("1. Ver libros disponibles")
    print("2. Buscar libros cortos (menos de 400 páginas)")
    print("3. Ver estadísticas")
    print("4. Agregar categoría")
    print("5. Salir")

    opcion = input("Elige una opción: ")

    if opcion == "1":
        disponibles = mostrar_disponibles(libros)
        print("\nLibros disponibles:")
        for libro in disponibles:
            print(f"- {libro['titulo']} de {libro['autor']}")

    elif opcion == "2":
        max_pag = int(input("Introduce el máximo de páginas: "))
        resultado = buscar_por_paginas(libros, max_pag)
        print("\nLibros encontrados:")
        for libro in resultado:
            print(f"- {libro['titulo']} ({libro['paginas']} páginas)")

    elif opcion == "3":
        total = contar_libros(libros)
        promedio = promedio_paginas(libros)
        print(f"\nTotal de libros: {total}")
        print(f"Promedio de páginas: {promedio:.2f}")

    elif opcion == "4":
        nueva = input("Introduce la nueva categoría: ")
        categorias_actualizadas = agregar_categoria(categorias, nueva)
        print("\nCategorías actuales:")
        for cat in categorias_actualizadas:
            print(f"- {cat}")

    elif opcion == "5":
        continuar = "n"
        print("Saliendo del sistema...")

    else:
        print("Opción no válida.")
