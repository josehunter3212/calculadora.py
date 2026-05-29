#!/usr/bin/env python3
from tkinter import *
import math

expr = ""  # Cadena global que almacena la expresión matemática


def press(key):
    global expr
    # Si se presiona un operador visual, lo mapeamos al operador real de Python
    if key == 'x':
        expr += '*'
    elif key == '÷':
        expr += '/'
    elif key == '^':
        expr += '**'
    else:
        expr += str(key)

    # Mostramos en pantalla los símbolos limpios y legibles para el usuario
    display.set(expr.replace('**', '^').replace('*', 'x').replace('/', '÷'))


def equal():
    global expr
    try:
        # eval() procesará la expresión con floats de forma nativa si hay decimales
        result = str(eval(expr))

        # Formateo estético: si el resultado termina en .0, lo mostramos simplificado
        if result.endswith('.0'):
            result = result[:-2]

        display.set(result)
        expr = result  # Permite seguir operando con el resultado anterior
    except ZeroDivisionError:
        display.set("Error: Div ÷ 0")
        expr = ""
    except Exception:
        display.set("Error")
        expr = ""


def press_sqrt():
    global expr
    try:
        # Evaluamos primero lo que esté en pantalla antes de aplicar la raíz
        val = float(eval(expr)) if expr else 0.0
        if val < 0:
            display.set("Error: √ Negativa")
            expr = ""
        else:
            res = math.sqrt(val)
            res_str = str(res)
            if res_str.endswith('.0'):
                res_str = res_str[:-2]
            display.set(res_str)
            expr = res_str
    except Exception:
        display.set("Error")
        expr = ""


def clear():
    global expr
    expr = ""
    display.set("")


if __name__ == "__main__":
    root = Tk()
    root.configure(bg="light green")
    root.title("Calculadora Completa")
    root.geometry("270x200")  # Ajustado el alto para añadir los nuevos botones

    display = StringVar()
    entry = Entry(root, textvariable=display, justify="right", font=("Arial", 12))
    entry.grid(row=0, column=0, columnspan=4, ipadx=4, ipady=8, padx=5, pady=5, sticky="nsew")

    # --- BOTONES DE NÚMEROS ---
    btn1 = Button(root, text='1', fg='black', bg='red', command=lambda: press(1), height=1, width=7)
    btn1.grid(row=2, column=0)
    btn2 = Button(root, text='2', fg='black', bg='red', command=lambda: press(2), height=1, width=7)
    btn2.grid(row=2, column=1)
    btn3 = Button(root, text='3', fg='black', bg='red', command=lambda: press(3), height=1, width=7)
    btn3.grid(row=2, column=2)

    btn4 = Button(root, text='4', fg='black', bg='red', command=lambda: press(4), height=1, width=7)
    btn4.grid(row=3, column=0)
    btn5 = Button(root, text='5', fg='black', bg='red', command=lambda: press(5), height=1, width=7)
    btn5.grid(row=3, column=1)
    btn6 = Button(root, text='6', fg='black', bg='red', command=lambda: press(6), height=1, width=7)
    btn6.grid(row=3, column=2)

    btn7 = Button(root, text='7', fg='black', bg='red', command=lambda: press(7), height=1, width=7)
    btn7.grid(row=4, column=0)
    btn8 = Button(root, text='8', fg='black', bg='red', command=lambda: press(8), height=1, width=7)
    btn8.grid(row=4, column=1)
    btn9 = Button(root, text='9', fg='black', bg='red', command=lambda: press(9), height=1, width=7)
    btn9.grid(row=4, column=2)

    btn0 = Button(root, text='0', fg='black', bg='red', command=lambda: press(0), height=1, width=7)
    btn0.grid(row=5, column=0)

    # --- BOTONES DE OPERADORES BÁSICOS ---
    plus = Button(root, text='+', fg='black', bg='red', command=lambda: press('+'), height=1, width=7)
    plus.grid(row=2, column=3)
    minus = Button(root, text='-', fg='black', bg='red', command=lambda: press('-'), height=1, width=7)
    minus.grid(row=3, column=3)
    mult = Button(root, text='x', fg='black', bg='red', command=lambda: press('x'), height=1, width=7)
    mult.grid(row=4, column=3)
    div = Button(root, text='÷', fg='black', bg='red', command=lambda: press('÷'), height=1, width=7)
    div.grid(row=5, column=3)

    # --- NUEVOS OPERADORES Y BOTONES DE CONTROL ---
    pow_btn = Button(root, text='xⁿ', fg='black', bg='red', command=lambda: press('^'), height=1, width=7)
    pow_btn.grid(row=6, column=2)

    sqrt_btn = Button(root, text='√n', fg='black', bg='red', command=press_sqrt, height=1, width=7)
    sqrt_btn.grid(row=6, column=3)

    dot = Button(root, text='.', fg='black', bg='red', command=lambda: press('.'), height=1, width=7)
    dot.grid(row=5, column=1)

    eq = Button(root, text='=', fg='black', bg='red', command=equal, height=1, width=7)
    eq.grid(row=5, column=2)

    clr = Button(root, text='Clear', fg='black', bg='red', command=clear, height=1, width=7)
    clr.grid(row=6, column=0, columnspan=2, sticky="we")  # Ocupa dos columnas para equilibrar la estética

    root.mainloop()
