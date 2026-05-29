# Se importan los módulos aquí más adelante
# from modulos import datos, validaciones, busquedas, filtros, ordenamiento, estadisticas

def mostrar_menu():
    print("\n--- SISTEMA DE GESTIÓN DE PAÍSES ---")
    print("1. Agregar un país")
    print("2. Actualizar Población y Superficie")
    print("3. Buscar un país")
    print("4. Filtrar países")
    print("5. Ordenar países")
    print("6. Mostrar estadísticas")
    print("7. Salir")
    return input("Seleccione una opción: ")

def main():
    # Paso 1: Cargar los datos del CSV a una lista de diccionarios
    # lista_paises = datos.cargar_csv("Paises.csv")
    lista_paises = [] # Placeholder temporal
    
    while True:
        opcion = mostrar_menu()
        
        if opcion == '1':
            print("Lógica para agregar país...")
            # datos.agregar_pais(lista_paises)
            
        elif opcion == '2':
            print("Lógica para actualizar país...")
            
        elif opcion == '3':
            print("Lógica para buscar país...")
            
        elif opcion == '4':
            print("Lógica para filtrar países...")
            
        elif opcion == '5':
            print("Lógica para ordenar países...")
            
        elif opcion == '6':
            print("Lógica para mostrar estadísticas...")
            
        elif opcion == '7':
            print("Guardando datos y saliendo del sistema... ¡Hasta luego!")
            # datos.guardar_csv("Paises.csv", lista_paises)
            break
            
        else:
            print("Opción inválida. Por favor, intente nuevamente.")

# Este bloque asegura que el script principal se ejecute correctamente
if __name__ == "__main__":
    main()