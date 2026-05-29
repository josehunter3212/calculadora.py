#!/usr/bin/env python3
import os
import math

def limpiar_pantalla():
    """Limpia la consola de comandos de forma nativa en Linux/Debian."""
    os.system('clear')

def pausar():
    """Detiene el flujo para que el usuario pueda ver el resultado obtenido."""
    print("\n-------------------------------------------------")
    input("Presione una tecla para volver al menú...")

def mostrar_menu():
    """Imprime la interfaz de usuario basada en texto (TUI)."""
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
    """Fuerza la entrada de datos tipo float y evita cierres por error de escritura."""
    while True:
        try:
            return float(input(mensaje))
        except ValueError:
            print("❌ Error: Tipo de dato inválido. Ingrese un número (entero o decimal).")

def iniciar_calculadora():
    """Manejador principal del flujo secuencial de la TUI."""
    while True:
        limpiar_pantalla()
        mostrar_menu()
        
        opcion = input("Seleccione una opción (1-7): ").strip()
        
        # Condición de salida única del sistema
        if opcion == '7':
            limpiar_pantalla()
            print("\n¡Programa finalizado correctamente! Hasta luego.\n")
            break
            
        # Bloque para operaciones de dos números (Suma, Resta, Multiplicación, División, Potencia)
        if opcion in ['1', '2', '3', '4', '5']:
            limpiar_pantalla()
            print(f"--- [OPERACIÓN SELECCIONADA: Opción {opcion}] ---\n")
            
            num1 = solicitar_numero("Ingrese el primer número (float): ")
            num2 = solicitar_numero("Ingrese el segundo número (float): ")
            
            print("\n---------------- RESULTADO ----------------")
            if opcion == '1':
                print(f"Resultado: {num1} + {num2} = {num1 + num2}")
            elif opcion == '2':
                print(f"Resultado: {num1} - {num2} = {num1 - num2}")
            elif opcion == '3':
                print(f"Resultado: {num1} x {num2} = {num1 * num2}")
            elif opcion == '4':
                if num2 == 0:
                    print("❌ Error: Indeterminación. No se puede dividir entre cero (0).")
                else:
                    print(f"Resultado: {num1} ÷ {num2} = {num1 / num2}")
            elif opcion == '5':
                # Operador nativo de potencia en Python
                print(f"Resultado: {num1}^{num2} = {num1 ** num2}")
                
            pausar()

        # Bloque para operación de un solo número (Raíz Cuadrada)
        elif opcion == '6':
            limpiar_pantalla()
            print("--- [OPERACIÓN SELECCIONADA: Opción 6 (Raíz Cuadrada)] ---\n")
            
            num = solicitar_numero("Ingrese el número (float): ")
            
            print("\n---------------- RESULTADO ----------------")
            if num < 0:
                print("❌ Error: No se puede calcular la raíz cuadrada de un número negativo.")
            else:
                # Uso de la función nativa de la biblioteca 'math'
                print(f"Resultado: √({num}) = {math.sqrt(num)}")
                
            pausar()
            
        else:
            print("\n❌ Opción no válida. Intente con un número del 1 al 7.")
            input("\nPresione una tecla para continuar...")

# Punto de entrada estándar para scripts ejecutables
if __name__ == "__main__":
    iniciar_calculadora()
