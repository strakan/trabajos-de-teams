import math  # Importar la librería matemática para usar π

# Programa para calcular el área y la circunferencia de un círculo
def calcular_circulo():
    try:
        # Solicitar el radio del círculo al usuario
        radio = float(input("Ingresa el radio del círculo: "))

        if radio < 0:
            print("El radio no puede ser negativo. Por favor, ingresa un valor positivo.")
        else:
            # Calcular el área: A = π * r^2
            area = math.pi * (radio ** 2)

            # Calcular la circunferencia: C = 2 * π * r
            circunferencia = 2 * math.pi * radio

            # Mostrar los resultados
            print(f"El área del círculo es: {area:.2f}")
            print(f"La circunferencia del círculo es: {circunferencia:.2f}")
    except ValueError:
        print("Error: Ingresa un número válido para el radio.")

# Llamar a la función
calcular_circulo()

