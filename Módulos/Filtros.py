def filtrar_por_continente(lista_paises, continente_buscado):
    """
    Recibe la lista completa y devuelve una nueva lista solo con los países
    que pertenecen al continente especificado
    """
    resultados = []
    continente_limpio = continente_buscado.lower().strip()
    
    for pais in lista_paises:
        if pais["continente"].lower() == continente_limpio:
            resultados.append(pais)
            
    return resultados


def filtrar_por_rango_poblacion(lista_paises, min_poblacion, max_poblacion):
    """
    Filtra los países cuya población se encuentre dentro del rango especificado (min y max)
    """
    resultados = []
    for pais in lista_paises:
        if min_poblacion <= pais["poblacion"] <= max_poblacion:
            resultados.append(pais)
            
    return resultados


def filtrar_por_rango_superficie(lista_paises, min_superficie, max_superficie):
    """
    Filtra los países cuya superficie se encuentre dentro del rango especificado (min y max)
    """
    resultados = []
    for pais in lista_paises:
        if min_superficie <= pais["superficie"] <= max_superficie:
            resultados.append(pais)
            
    return resultados