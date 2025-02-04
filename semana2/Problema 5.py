# Programa para verificar si un número es primo
def es_primo():
    try:
        # Solicitar el número al usuario
        numero = int(input("Ingresa un número para verificar si es primo: "))

        # Los números menores que 2 no son primos
        if numero < 2:
            print(f"{numero} no es un número primo.")
        else:
            # Verificar si el número tiene divisores aparte de 1 y sí mismo
            es_primo = True
            for i in range(2, int(numero ** 0.5) + 1):  # Revisar hasta la raíz cuadrada del número
                if numero % i == 0:
                    es_primo = False
                    break
            if es_primo:
                print(f"{numero} es un número primo.")
            else:
                print(f"{numero} no es un número primo.")
    except ValueError:
        print("Error: Ingresa un número entero válido.")

# Llamar a la función para verificar si es primo
es_primo()
