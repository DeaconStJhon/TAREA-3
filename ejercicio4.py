from funciones import dividir_numeros

while True:
    try:
        num1 = float(input("Ingrese el primer número: "))
        num2 = float(input("Ingrese el segundo número: "))
        resultado = dividir_numeros(num1, num2)
        print(f"Resultado de la división: {resultado}")
        break
    except ValueError as e:
        print(f"Error: {e}. Por favor, ingrese números válidos.")
    except ZeroDivisionError:
        print("Error: No se puede dividir por cero. Por favor, ingrese otro número.")