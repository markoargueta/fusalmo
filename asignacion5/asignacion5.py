import calculadora

import os
def clear():
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")

continuar = 1

try:
    while continuar!=0:
        clear()
        print(""" Calculadora
        1 Suma.
        2 Resta.
        3 Multiplicación.
        4 División.
        5 Módulo.
        6 Potencia.
        7 Raíz Cuadrada.
        8 Factorial.
        0 Salir
        """)
        operacion = int(input("Escriba el número de la opción: "))

        if operacion == 1:
            num1 = int(input("Escriba el número 1: "))
            num2 = int(input("Escriba el número 2: "))
            calculadora.suma(num1,num2)
        if operacion == 2:
            num1 = int(input("Escriba el número 1: "))
            num2 = int(input("Escriba el número 2: "))
            calculadora.resta(num1,num2)
        if operacion == 3:
            num1 = int(input("Escriba el número 1: "))
            num2 = int(input("Escriba el número 2: "))
            calculadora.multiplicacion(num1,num2)
        if operacion == 4:
            num1 = int(input("Escriba el número 1: "))
            num2 = int(input("Escriba el número 2: "))
            calculadora.division(num1,num2)
        if operacion == 5:
            num1 = int(input("Escriba el número 1: "))
            num2 = int(input("Escriba el número 2: "))
            calculadora.modulo(num1,num2)
        if operacion == 6:
            num1 = int(input("Escriba el número a elevar: "))
            num2 = int(input("Escriba la potencia: "))
            calculadora.potencia(num1,num2)
        if operacion == 7:
            num1 = int(input("Escriba el número a obtener raíz cuadrada: "))
            calculadora.raiz(num1)
        if operacion == 8:
            num1 = int(input("Escriba el número a obtener el factorial: "))
            calculadora.fact(num1)

        if operacion<0 or operacion>8:
            print("Opción no válida")

        seguir = int(input("¿Desea realizar otra operación? 1 para continuar; 0 para salir. "))
        if seguir == 1:
            continuar = 1
        elif seguir == 0:
            continuar=0
        else:
            print("Opción no válida, adiós")
            continuar=0

except (KeyboardInterrupt, ValueError):
    print("Opción no válida, adiós")