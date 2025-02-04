# Calculadora simple
def calculadora():
    print("Bienvenido a la calculadora simple")
    print("Operaciones disponibles:")
    print("1. Suma")
    print("2. Resta")
    print("3. Multiplicación")
    print("4. División")

    # Solicitar al usuario que elija una operación
    opcion = input("Elige una operación (1/2/3/4): ")

    # Solicitar al usuario los números para la operación
    try:
        num1 = float(input("Ingresa el primer número: "))
        num2 = float(input("Ingresa el segundo número: "))

        # Realizar la operación seleccionada
        if opcion == "1":
            resultado = num1 + num2
            print(f"El resultado de la suma es: {resultado}")
        elif opcion == "2":
            resultado = num1 - num2
            print(f"El resultado de la resta es: {resultado}")
        elif opcion == "3":
            resultado = num1 * num2
            print(f"El resultado de la multiplicación es: {resultado}")
        elif opcion == "4":
            if num2 != 0:
                resultado = num1 / num2
                print(f"El resultado de la división es: {resultado}")
            else:
                print("Error: No se puede dividir entre cero.")
        else:
            print("Opción no válida. Por favor, elige una operación válida.")
    except ValueError:
        print("Error: Por favor ingresa un número válido.")

# Llamar a la función calculadora
calculadora()


