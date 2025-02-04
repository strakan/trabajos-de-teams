# Programa para calcular el interés compuesto
def calcular_interes_compuesto():
    try:
        # Solicitar los valores al usuario
        capital = float(input("Ingresa el capital inicial: "))
        tasa = float(input("Ingresa la tasa de interés anual (en porcentaje): "))
        tiempo = int(input("Ingresa el tiempo en años: "))
        n = int(input("Ingresa el número de veces que se capitaliza el interés por año: "))

        # Convertir la tasa de interés a decimal
        tasa_decimal = tasa / 100

        # Fórmula del interés compuesto: A = P(1 + r/n)^(n*t)
        monto_final = capital * (1 + tasa_decimal / n) ** (n * tiempo)

        # Cálculo del interés ganado
        interes_ganado = monto_final - capital

        # Mostrar resultados
        print(f"Monto final después de {tiempo} años: ${monto_final:.2f}")
        print(f"Interés compuesto ganado: ${interes_ganado:.2f}")
    except ValueError:
        print("Error: Ingresa valores numéricos válidos.")

# Llamar a la función para calcular el interés compuesto
calcular_interes_compuesto()
