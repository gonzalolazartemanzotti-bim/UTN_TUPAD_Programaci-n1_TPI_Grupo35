import csv

def cargar_csv(ruta_archivo):
    """
    Lee un archivo CSV y retorna una lista de diccionarios
    Maneja excepciones si el archivo no existe o si hay errores de formato numérico
    """
    lista_paises = []
    
    try:
        # Se abre el archivo en modo lectura ('r')
        with open(ruta_archivo, mode='r', encoding='utf-8') as archivo:
            lector = csv.DictReader(archivo)
            
            # Se limpian los nombres de las columnas por si hay espacios accidentales en el CSV
            lector.fieldnames = [campo.strip() for campo in lector.fieldnames]
            
            for fila in lector:
                try:
                    # Se crea el diccionario asegurando la conversión de tipos
                    pais = {
                        "nombre": fila["nombre"].strip(),
                        "poblacion": int(fila["poblacion"].strip()),
                        "superficie": int(fila["superficie"].strip()),
                        "continente": fila["continente"].strip()
                    }
                    lista_paises.append(pais)
                    
                except ValueError:
                    # Se captura el error si no se puede convertir a entero (int)
                    nombre_error = fila.get("nombre", "Desconocido").strip()
                    print(f"Error de formato en los datos del país: {nombre_error}. Se omitirá este registro.")
                    
        print(f"Se cargaron {len(lista_paises)} países correctamente.")
        
    except FileNotFoundError:
        # Captura el error si el archivo CSV no se encuentra en la ruta indicada
        print(f"Error: No se encontró el archivo '{ruta_archivo}'. Iniciando con una base de datos vacía.")
        
    except Exception as e:
        # Captura cualquier otro error inesperado
        print(f"Ocurrió un error inesperado al leer el archivo: {e}")
        
    return lista_paises


def guardar_csv(ruta_archivo, lista_paises):
    """
    Guarda la lista de diccionarios actual sobreescribiendo el archivo CSV
    """
    try:
        # Se abre el archivo en modo escritura ('w')
        with open(ruta_archivo, mode='w', encoding='utf-8', newline='') as archivo:
            # Se definen los encabezados
            campos = ["nombre", "poblacion", "superficie", "continente"]
            escritor = csv.DictWriter(archivo, fieldnames=campos)
            
            # Se escribe la primera fila (encabezados) y luego los datos
            escritor.writeheader()
            for pais in lista_paises:
                escritor.writerow(pais)
                
        print("Datos guardados exitosamente en el archivo CSV.")
        
    except Exception as e:
        print(f"Error al intentar guardar los datos: {e}")


import Validaciones

def agregar_pais(lista_paises):
    """
    Permite al usuario ingresar un nuevo país y lo agrega a la lista
    Utiliza el módulo Validaciones para asegurar que no haya campos vacíos ni tipos incorrectos
    """
    print("\n--- Agregar Nuevo País ---")
    
    nombre = Validaciones.pedir_cadena("Ingrese el nombre del país: ")
    
    # Se valida que el país no exista previamente para evitar duplicados
    for pais in lista_paises:
        if pais["nombre"].lower() == nombre.lower():
            print("Error: El país ya existe en la base de datos.")
            return

    poblacion = Validaciones.pedir_entero("Ingrese la población: ")
    superficie = Validaciones.pedir_entero("Ingrese la superficie en km2: ")
    continente = Validaciones.pedir_cadena("Ingrese el continente: ")
    
    nuevo_pais = {
        "nombre": nombre,
        "poblacion": poblacion,
        "superficie": superficie,
        "continente": continente
    }
    
    lista_paises.append(nuevo_pais)
    print(f"Éxito: {nombre} ha sido agregado correctamente a la lista temporal.")


def actualizar_pais(lista_paises):
    """
    Busca un país por nombre exacto y permite modificar su población y superficie
    """
    print("\n--- Actualizar Datos de un País ---")
    
    nombre_buscado = Validaciones.pedir_cadena("Ingrese el nombre exacto del país a actualizar: ")
    pais_encontrado = None
    
    # Se busca el país exacto
    for pais in lista_paises:
        if pais["nombre"].lower() == nombre_buscado.lower():
            pais_encontrado = pais
            break
            
    if pais_encontrado:
        print(f"País encontrado: {pais_encontrado['nombre']}")
        
        # Se piden los nuevos datos mostrando los actuales como referencia
        nueva_poblacion = Validaciones.pedir_entero(f"Ingrese la nueva población (Actual: {pais_encontrado['poblacion']}): ")
        nueva_superficie = Validaciones.pedir_entero(f"Ingrese la nueva superficie en km2 (Actual: {pais_encontrado['superficie']}): ")
        
        # Se actualizan los valores en el diccionario
        pais_encontrado["poblacion"] = nueva_poblacion
        pais_encontrado["superficie"] = nueva_superficie
        
        print("Éxito: Los datos del país han sido actualizados correctamente.")
    else:
        print("Error: No se encontró un país con ese nombre en la base de datos.")