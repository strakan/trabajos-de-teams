# Programa para generar listas de números pares e impares
def generar_pares_impares():
    try:
        # Solicitar el límite al usuario
        limite = int(input("Ingresa el límite para generar los números: "))

        if limite < 0:
            print("Por favor, ingresa un número positivo.")
        else:
            # Generar lista de números pares
            pares = [num for num in range(limite + 1) if num % 2 == 0]

            # Generar lista de números impares
            impares = [num for num in range(limite + 1) if num % 2 != 0]

            # Mostrar las listas
            print(f"Números pares hasta {limite}: {pares}")
            print(f"Números impares hasta {limite}: {impares}")
    except ValueError:
        print("Error: Ingresa un número entero válido.")

# Llamar a la función
generar_pares_impares()
