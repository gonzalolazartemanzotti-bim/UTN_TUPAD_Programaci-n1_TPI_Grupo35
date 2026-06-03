# Se importan todos los módulos desde la subcarpeta "Módulos"
from Módulos import Datos
from Módulos import Validaciones
from Módulos import Búsquedas
from Módulos import Filtros
from Módulos import Ordenamiento
from Módulos import Estadísticas

def mostrar_menu():
    """Muestra las opciones principales del sistema."""
    print("\n" + "="*40)
    print("   SISTEMA DE GESTIÓN DE PAÍSES   ")
    print("="*40)
    print("1. Agregar un país")
    print("2. Actualizar Población y Superficie")
    print("3. Buscar un país")
    print("4. Filtrar países")
    print("5. Ordenar países")
    print("6. Mostrar estadísticas")
    print("7. Guardar y Salir")
    print("="*40)
    return input("Seleccione una opción: ").strip()

def main():
    # Se define la ruta de nuestro archivo base
    ruta_archivo = "Paises.csv"
    
    # Se cargan los datos al iniciar el programa
    print("Iniciando sistema...")
    lista_paises = Datos.cargar_csv(ruta_archivo)
    
    while True:
        opcion = mostrar_menu()
        
        if opcion == '1':
            Datos.agregar_pais(lista_paises)
            
        elif opcion == '2':
            Datos.actualizar_pais(lista_paises)
            
        elif opcion == '3':
            nombre = Validaciones.pedir_cadena("Ingrese el nombre a buscar: ")
            resultados = Búsquedas.buscar_por_nombre(lista_paises, nombre)
            Búsquedas.mostrar_resultados(resultados)
            
        elif opcion == '4':
            print("\n--- Submenú de Filtros ---")
            print("a. Por Continente")
            print("b. Por rango de Población")
            print("c. Por rango de Superficie")
            sub_op = input("Elija una opción (a/b/c): ").strip().lower()
            
            if sub_op == 'a':
                continente = Validaciones.pedir_cadena("Ingrese el continente: ")
                res = Filtros.filtrar_por_continente(lista_paises, continente)
                Búsquedas.mostrar_resultados(res)
            elif sub_op == 'b':
                min_p = Validaciones.pedir_entero("Población mínima: ")
                max_p = Validaciones.pedir_entero("Población máxima: ")
                res = Filtros.filtrar_por_rango_poblacion(lista_paises, min_p, max_p)
                Búsquedas.mostrar_resultados(res)
            elif sub_op == 'c':
                min_s = Validaciones.pedir_entero("Superficie mínima: ")
                max_s = Validaciones.pedir_entero("Superficie máxima: ")
                res = Filtros.filtrar_por_rango_superficie(lista_paises, min_s, max_s)
                Búsquedas.mostrar_resultados(res)
            else:
                print("Opción inválida.")
                
        elif opcion == '5':
            print("\n--- Submenú de Ordenamiento ---")
            print("a. Por Nombre")
            print("b. Por Población")
            print("c. Por Superficie")
            sub_op = input("Elija una opción (a/b/c): ").strip().lower()
            
            desc = input("¿Orden descendente? (s/n): ").strip().lower() == 's'
            
            if sub_op == 'a':
                lista_paises = Ordenamiento.ordenar_por_nombre(lista_paises, desc)
            elif sub_op == 'b':
                lista_paises = Ordenamiento.ordenar_por_poblacion(lista_paises, desc)
            elif sub_op == 'c':
                lista_paises = Ordenamiento.ordenar_por_superficie(lista_paises, desc)
            else:
                print("Opción inválida.")
                continue
                
            print("\nLista ordenada correctamente. A continuación los primeros 10 resultados:")
            Búsquedas.mostrar_resultados(lista_paises[:10])
            
        elif opcion == '6':
            print("\n--- Estadísticas del Sistema ---")
            mayor, menor = Estadísticas.obtener_extremos_poblacion(lista_paises)
            if mayor and menor:
                print(f"País con mayor población: {mayor['nombre']} ({mayor['poblacion']})")
                print(f"País con menor población: {menor['nombre']} ({menor['poblacion']})")
                
            prom_pob, prom_sup = Estadísticas.calcular_promedios(lista_paises)
            print(f"Promedio de población: {prom_pob:.2f}")
            print(f"Promedio de superficie: {prom_sup:.2f} km2")
            
            print("\nCantidad de países por continente:")
            conteo = Estadísticas.contar_por_continente(lista_paises)
            for cont, cant in conteo.items():
                print(f"- {cont}: {cant}")
                
        elif opcion == '7':
            print("\nGuardando cambios en el archivo CSV...")
            Datos.guardar_csv(ruta_archivo, lista_paises)
            print("¡Gracias por utilizar el sistema! Hasta luego.")
            break
            
        else:
            print("Opción no válida. Por favor, intente de nuevo.")

# Punto de entrada de la aplicación
if __name__ == "__main__":
    main()