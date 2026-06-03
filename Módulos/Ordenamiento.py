def ordenar_por_nombre(lista_paises, descendente=False):
    """
    Ordena la lista de países alfabéticamente por su nombre
    Si descendente es True, ordena de la Z a la A
    """
    return sorted(lista_paises, key=lambda pais: pais["nombre"].lower(), reverse=descendente)


def ordenar_por_poblacion(lista_paises, descendente=False):
    """
    Ordena la lista de países según su población
    Si descendente es True, ordena de mayor a menor
    """
    return sorted(lista_paises, key=lambda pais: pais["poblacion"], reverse=descendente)


def ordenar_por_superficie(lista_paises, descendente=False):
    """
    Ordena la lista de países según su superficie en km2
    Si descendente es True, ordena de mayor a menor
    """
    return sorted(lista_paises, key=lambda pais: pais["superficie"], reverse=descendente)