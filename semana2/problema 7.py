# Programa para determinar si un número es par, impar o múltiplo de otro
def determinar_paridad_y_multiplo():
    try:
        # Solicitar los números al usuario
        numero = int(input("Ingresa un número: "))
        otro_numero = int(input("Ingresa otro número para verificar si es múltiplo: "))

        # Determinar si el número es par o impar
        if numero % 2 == 0:
            print(f"{numero} es un número par.")
        else:
            print(f"{numero} es un número impar.")

        # Determinar si el número es múltiplo de otro
        if otro_numero != 0:  # Validar que no se divida entre 0
            if numero % otro_numero == 0:
                print(f"{numero} es múltiplo de {otro_numero}.")
            else:
                print(f"{numero} no es múltiplo de {otro_numero}.")
        else:
            print("No se puede verificar si es múltiplo porque el segundo número es 0.")
    except ValueError:
        print("Error: Ingresa números enteros válidos.")

# Llamar a la función
determinar_paridad_y_multiplo()
