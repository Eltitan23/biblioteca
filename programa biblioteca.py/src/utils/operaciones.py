from models.libro import Libro

def promedio_paginas(libros: list[Libro]):
    """Calcula el promedio de páginas de todos los libros"""
    total_paginas = 0

    for libro in libros:
        total_paginas += libro["paginas"]

    return total_paginas / len(libros)

def mostrar_disponibles(lista_libros: list[Libro]):
    """Muestra solo los libros que están disponibles"""
    disponibles = []

    for libro in lista_libros:
        if libro["disponible"]:
            disponibles.append(libro)

    return disponibles


def buscar_por_paginas(lista_libros: list[Libro], max_paginas: int):
    """Muestra libros con menos páginas que max_paginas"""
    libros_filtrados = []

    for libro in lista_libros:
        if libro["paginas"] < max_paginas:
            libros_filtrados.append(libro)

    return libros_filtrados


def agregar_categoria(set_categorias: set[str], nueva_categoria: str):
    """Agrega una nueva categoría al set"""
    if nueva_categoria not in set_categorias:
        set_categorias.add(nueva_categoria)

    return set_categorias