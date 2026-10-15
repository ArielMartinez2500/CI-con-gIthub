
def celsius_a_fahrenheit(c):
    """
    Convierte una temperatura de Celsius a Fahrenheit.

    Args:
        c (int | float): Temperatura en Celsius.

    Returns:
        float: Temperatura en Fahrenheit.

    Raises:
        TypeError: Si el valor no es numérico.
    """
    if isinstance(c, bool) or not isinstance(c, (int, float)):
        raise TypeError("La temperatura debe ser un número.")

    return (c * 9 / 5) + 32


def solicitar_temperatura():
    """
    Solicita al usuario una temperatura en Celsius.

    Returns:
        float: Temperatura ingresada por el usuario.
    """
    while True:
        try:
            temperatura = float(input(
                "\nIngresa la temperatura en Celsius: "
            ))
            return temperatura

        except ValueError:
            print("Error: Debes ingresar un número válido.")


def mostrar_conversion():
    """
    Solicita una temperatura y muestra su conversión.
    """
    celsius = solicitar_temperatura()
    fahrenheit = celsius_a_fahrenheit(celsius)

    print("\n--- RESULTADO ---")
    print(f"Temperatura en Celsius: {celsius:.2f} °C")
    print(f"Temperatura en Fahrenheit: {fahrenheit:.2f} °F")


def mostrar_menu():
    """
    Muestra el menú principal del programa.
    """
    while True:
        print("\n================================")
        print("   CONVERSOR DE TEMPERATURA")
        print("================================")
        print("1. Convertir Celsius a Fahrenheit")
        print("2. Salir")
        print("================================")

        opcion = input("Selecciona una opción: ")

        if opcion == "1":
            mostrar_conversion()

        elif opcion == "2":
            print("\nGracias por utilizar el conversor.")
            break

        else:
            print("\nOpción incorrecta. Intenta nuevamente.")


if __name__ == "__main__":
    mostrar_menu()
