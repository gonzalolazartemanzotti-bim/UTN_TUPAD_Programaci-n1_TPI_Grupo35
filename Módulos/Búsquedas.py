def buscar_por_nombre(lista_paises, nombre_buscado):
    """
    Busca un país por nombre considerando coincidencias exactas o parciales
    Retorna una lista con los países encontrados (ya que una búsqueda parcial puede devolver más de uno)
    """
    resultados = []
    # Se convierte la búsqueda a minúsculas para que no sea sensible a mayúsculas
    busqueda_limpia = nombre_buscado.lower().strip()
    
    for pais in lista_paises:
        # CSe convierte también el nombre del país a minúsculas para comparar
        nombre_pais = pais["nombre"].lower()
        
        # 'in' permite detectar coincidencias parciales (ej: "arg" encuentra "Argentina")
        if busqueda_limpia in nombre_pais:
            resultados.append(pais)
            
    return resultados


def mostrar_resultados(resultados):
    """
    Recibe una lista de resultados de búsqueda y los imprime con un formato legible.
    """
    if not resultados:
        print("No se encontraron países que coincidan con la búsqueda.")
        return
        
    print("\n--- Resultados de la Búsqueda ---")
    for pais in resultados:
        print(f"Nombre: {pais['nombre']} | Continente: {pais['continente']} | Población: {pais['poblacion']} | Superficie: {pais['superficie']} km2")
    print("---------------------------------")