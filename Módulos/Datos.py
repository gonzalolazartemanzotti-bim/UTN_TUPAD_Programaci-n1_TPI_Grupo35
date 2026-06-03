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