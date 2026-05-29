#!/usr/bin/env python3
import os
import math


def limpiar_pantalla():
    """Limpia la consola de comandos en Linux/Debian."""
    os.system('clear')


def pausar():
    """Detiene la ejecución hasta que el usuario presione Enter."""
    print("\n-------------------------------------------------")
    input("Presione [Enter] para volver al menú...")


def mostrar_menu():
    """Muestra el menú de la interfaz de texto (TUI)."""
    print("=========================================")
    print("         CALCULADORA TUI - PYTHON        ")
    print("=========================================")
    print(" 1. Suma (+)")
    print(" 2. Resta (-)")
    print(" 3. Multiplicación (x)")
    print(" 4. División (÷)")
    print(" 5. Potencia (x^n)")
    print(" 6. Raíz cuadrada (√n)")
    print(" 7. Salir")
    print("=========================================")


def solicitar_numero(mensaje):
    """Solicita un número float y maneja errores si el usuario ingresa texto."""
    while True:
        try:
            return float(input(mensaje))
        except ValueError:
            print("❌ Error: Por favor, introduce un número decimal o entero válido.")


def ejecutar_calculadora():
    """Bucle principal que controla la lógica de la TUI."""
    while True:
        limpiar_pantalla()
        mostrar_menu()

        opcion = input("Seleccione una opción (1-7): ").strip()

        # Opción de salida inmediata
        if opcion == '7':
            limpiar_pantalla()
            print("\n¡Gracias por usar la calculadora! Saliendo del programa...\n")
            break

        # Operaciones de dos números (1 a 5)
        if opcion in ['1', '2', '3', '4', '5']:
            limpiar_pantalla()
            print(f"--- Operación seleccionada: Opción {opcion} ---\n")

            num1 = solicitar_numero("Introduce el primer número (float): ")
            num2 = solicitar_numero("Introduce el segundo número (float): ")

            print("\n---------------- RESULTADO ----------------")
            if opcion == '1':
                print(f"Resultado: {num1} + {num2} = {num1 + num2}")
            elif opcion == '2':
                print(f"Resultado: {num1} - {num2} = {num1 - num2}")
            elif opcion == '3':
                print(f"Resultado: {num1} x {num2} = {num1 * num2}")
            elif opcion == '4':
                if num2 == 0:
                    print("❌ Error: No se puede dividir entre cero.")
                else:
                    print(f"Resultado: {num1} ÷ {num2} = {num1 / num2}")
            elif opcion == '5':
                print(f"Resultado: {num1} ^ {num2} = {num1 ** num2}")

            pausar()

        # Operación de un solo número (6 - Raíz Cuadrada)
        elif opcion == '6':
            limpiar_pantalla()
            print("--- Operación seleccionada: Raíz Cuadrada ---\n")

            num = solicitar_numero("Introduce el número (float): ")

            print("\n---------------- RESULTADO ----------------")
            if num < 0:
                print("❌ Error: No se puede calcular la raíz cuadrada de un número negativo.")
            else:
                print(f"Resultado: √({num}) = {math.sqrt(num)}")

            pausar()

        else:
            print("\n❌ Opción no válida. Inténtalo de nuevo.")
            # Pequeña pausa para que el usuario alcance a leer que se equivocó de opción
            input("\nPresione [Enter] para continuar...")


# Punto de entrada del programa
if __name__ == "__main__":
    ejecutar_calculadora()
