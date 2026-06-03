def obtener_extremos_poblacion(lista_paises):
    """
    Busca y retorna el país con mayor población y el país con menor población
    """
    # Si la lista está vacía, Se retorna None para evitar errores de índice
    if not lista_paises:
        return None, None
    
    # Se incializan las variables de referencia con el primer país de la lista
    # Se asume temporalmente que el primero es el mayor y el menor a la vez
    pais_mayor = lista_paises[0]
    pais_menor = lista_paises[0]
    
    # Se recorre cada país en la lista para comparar su población
    for pais in lista_paises:
        # Si la población del país actual es mayor a la que teníamos guardada, se actualiza la variable
        if pais["poblacion"] > pais_mayor["poblacion"]:
            pais_mayor = pais
            
        # Si la población del país actual es menor a la que teníamos guardada, se actualiza la variable
        if pais["poblacion"] < pais_menor["poblacion"]:
            pais_menor = pais
            
    # Se retornan ambas variables como una tupla
    return pais_mayor, pais_menor


def calcular_promedios(lista_paises):
    """
    Calcula el promedio total de población y superficie del dataset actual
    Retorna ambos promedios
    """
    # Se verifica que la lista no esté vacía para no dividir por cero más adelante
    if not lista_paises:
        return 0, 0
        
    # Se incializan los acumuladores en cero
    total_poblacion = 0
    total_superficie = 0
    
    # Se obtiene la cantidad total de países para usarla como divisor
    cantidad_paises = len(lista_paises)
    
    # Se le suman los valores numéricos de cada país a nuestros acumuladores
    for pais in lista_paises:
        total_poblacion += pais["poblacion"]
        total_superficie += pais["superficie"]
        
    # Se calculan los promedios dividiendo los totales por la cantidad de países
    promedio_poblacion = total_poblacion / cantidad_paises
    promedio_superficie = total_superficie / cantidad_paises
    
    return promedio_poblacion, promedio_superficie


def contar_por_continente(lista_paises):
    """
    Cuenta cuántos países hay por cada continente
    Retorna un diccionario donde la clave es el continente y el valor es la cantidad
    """
    # Se crea un diccionario vacío para ir guardando los resultados
    conteo = {}
    
    for pais in lista_paises:
        # Se extrae el continente del país en la iteración actual
        continente = pais["continente"]
        
        # Si el continente ya existe en el diccionario, se le suma 1 a su contador
        if continente in conteo:
            conteo[continente] += 1
        # Si es la primera vez que se procesa este continente, se lo agrega al diccionario iniciando en 1
        else:
            conteo[continente] = 1
            
    return conteo