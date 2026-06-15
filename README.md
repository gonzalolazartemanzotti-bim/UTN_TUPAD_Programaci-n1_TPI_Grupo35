# Sistema de Gestión de Datos de Países en Python

**Universidad:** Universidad Tecnológica Nacional (UTN)
**Carrera:** Tecnicatura Universitaria en Programación a Distancia (TUPAD)
**Materia:** Programación 1
**Año/Cuatrimestre:** 2026 - 1er Cuatrimestre

### Integrantes del Equipo
* Gonzalo Lazarte Manzotti
* Sofía Elgadban

### Profesores
* **Profesor:** Ariel Enferrel
* **Tutor/Ayudante:** Tomás García

---

## Descripción del Proyecto
Este proyecto es una aplicación de consola desarrollada en Python que permite gestionar información sobre países. El sistema carga un dataset desde un archivo CSV y permite realizar operaciones de alta, modificación, búsquedas, filtrados (por continente, población y superficie), ordenamientos y cálculo de estadísticas básicas. El objetivo principal es la aplicación práctica de listas, diccionarios, modularización mediante funciones y manejo de archivos.

---

## Estructura del Proyecto
El código fue diseñado siguiendo el principio de modularización, dividiendo las responsabilidades en distintos archivos:

* Base.py: Punto de entrada de la aplicación y menú interactivo.
* Paises.csv: Base de datos de prueba.
* Módulos/:
  * Datos.py: Lectura/escritura del CSV y ABM de países.
  * Validaciones.py: Control de inputs del usuario.
  * Búsquedas.py: Lógica de coincidencia exacta y parcial.
  * Filtros.py: Filtrado por atributos y rangos matemáticos.
  * Ordenamiento.py: Clasificación ascendente y descendente.
  * Estadísticas.py: Cálculo de promedios, máximos, mínimos y conteos.

---

## Instrucciones de Ejecución
1. Clonar este repositorio en tu entorno local.
2. Asegurarse de tener instalado Python 3.x.
3. Abrir una terminal y navegar hasta la carpeta raíz del proyecto.
4. Ejecutar el archivo principal con el comando:

       python Base.py

(Nota: No requiere instalación de librerías de terceros, utiliza exclusivamente módulos nativos como csv y os).

---

## Ejemplos de Entrada y Salida

**Ejemplo de Búsqueda:**
> Seleccione una opción: 3
> Ingrese el nombre a buscar: arg
> 
> --- Resultados de la Búsqueda ---
> Nombre: Argentina | Continente: América | Población: 45376763 | Superficie: 2780400 km2

**Ejemplo de Estadísticas:**
> --- Estadísticas del Sistema ---
> País con mayor población: Brasil (213993437)
> País con menor población: Australia (25687041)
> Promedio de población: 92837306.00
> Promedio de superficie: 3183569.38 km2

---

## Enlaces Importantes
* **Documentación (PDF):** https://github.com/gonzalolazartemanzotti-bim/UTN_TUPAD_Programacion1_TPI_Grupo35/blob/78eaeb6ac8c0793ee556a50f912f98989127b2f7/Informe.pdf
* **Video Demostrativo:** https://youtu.be/KY1ehDQpXm4?si=tLFO6Xx8-EKCa0LI
