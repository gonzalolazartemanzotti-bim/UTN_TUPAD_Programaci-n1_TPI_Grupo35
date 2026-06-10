def pedir_entero(mensaje):
    """
    Solicita un número entero al usuario
    Se repite hasta que el usuario ingresa un valor numérico válido mayor a cero
    """
    while True:
        valor = input(mensaje).strip()
        try:
            numero = int(valor)
            if numero > 0:
                return numero
            else:
                print("Error: El número debe ser mayor a cero. Intente nuevamente.")
        except ValueError:
            print("Error: Debe ingresar un valor numérico entero válido. No se permiten letras ni símbolos.")


def pedir_cadena(mensaje):
    """
    Solicita una cadena de texto al usuario
    Se repite hasta que el usuario ingresa un texto válido (sin números ni símbolos)
    """
    while True:
        texto = input(mensaje).strip()
        
        # 1. Se verifica que no esté vacío
        if not texto:
            print("Error: Este campo no puede estar vacío. Intente nuevamente.")
            continue
            
        # 2. Se verifica que solo contenga letras (y espacios)
        # Se usa replace(" ", "") temporalmente para que isalpha no rechace países como "Estados Unidos"
        if texto.replace(" ", "").isalpha():
            return texto
        else:
            print("Error: El texto solo puede contener letras. No se permiten números ni símbolos. Intente nuevamente.")