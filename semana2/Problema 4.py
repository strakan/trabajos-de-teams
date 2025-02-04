# Programa para generar la secuencia de Fibonacci
def generar_fibonacci():
    try:
        # Solicitar el número de términos al usuario
        n = int(input("¿Cuántos términos de la secuencia de Fibonacci deseas generar? "))
        
        # Validar que el número de términos sea mayor a cero
        if n <= 0:
            print("Por favor, ingresa un número entero positivo.")
        else:
            # Inicializar los dos primeros términos
            fib1, fib2 = 0, 1
            print("Secuencia de Fibonacci:")
            for _ in range(n):
                print(fib1, end=" ")
                # Actualizar los valores para el siguiente término
                fib1, fib2 = fib2, fib1 + fib2
            print()  # Salto de línea al final
    except ValueError:
        print("Error: Ingresa un número entero válido.")

# Llamar a la función para generar la secuencia de Fibonacci
generar_fibonacci()
