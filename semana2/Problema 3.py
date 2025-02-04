# Programa para calcular el factorial de un número
def calcular_factorial():
    try:
        # Solicitar el número al usuario
        numero = int(input("Ingresa un número para calcular su factorial: "))
        
        # Validar que el número no sea negativo
        if numero < 0:
            print("El factorial no está definido para números negativos.")
        else:
            factorial = 1
            for i in range(1, numero + 1):
                factorial *= i
            print(f"El factorial de {numero} es: {factorial}")
    except ValueError:
        print("Error: Ingresa un número entero válido.")

# Llamar a la función para calcular el factorial
calcular_factorial()

