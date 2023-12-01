def get_user_input():
    try:
        num1 = float(input("Ingrese un numero: "))
        num2 = float(input("Ingrese otro numero: "))
        operation = input("Elija una operacion (+, -, *, /) o escriba 'exit' para salir: ")
        return num1, num2, operation
    except ValueError:
        print("Input invalido. Por favor ingrese numeros.")
        return get_user_input()

def ejecutar_operacion(user_input, callback):
    num1, num2, operation = user_input

    # Utilizando callbacks para invocar cada operación
    result = callback(num1, num2)

    print("Resultado:", result)

def main():
    # Definir funciones lambda para cada operación
    suma = lambda x, y: x + y
    resta = lambda x, y: x - y
    multiplicacion = lambda x, y: x * y
    division = lambda x, y: x / y if y != 0 else "Error: División por cero"

    # Crear diccionario para mapear operadores a funciones lambda
    operations = {
        '+': suma,
        '-': resta,
        '*': multiplicacion,
        '/': division
    }

    while True:
        user_input = get_user_input()

        if user_input[2].lower() == 'exit':
            print("Salir.")
            break

        print("\nCalculando...")

        if user_input[2] in operations:
            ejecutar_operacion(user_input, operations[user_input[2]])
        else:
            print("Operacion invalida. Seleccione (+, -, *, /) o  escriba 'exit' para salir.")

if __name__ == "__main__":
    main()