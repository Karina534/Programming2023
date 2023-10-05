import math
import tkinter as tk
from tkinter import messagebox
def sqrt(num):
    #num = num[:-1]
    if int(num) < 0:
        messagebox.showinfo('Ты лох', "Нет корня из отрицательного числа")
    else:
        return (int(num)**0.5)
def clear():
    calc.delete(0, tk.END)
def calculate():
    value = calc.get()
    try:
        if value[-1] == '!':
            value = value[:-1]
            calc.delete(0, tk.END)
            calc.insert(0, sqrt(value))
        else:
            calc.delete(0, tk.END)
            calc.insert(0, eval(value))
    except ZeroDivisionError:
        messagebox.showinfo('Ты лох', "На ноль делить нельзя!")
        calc.insert(0, 0)

def add_num(num):
    value = calc.get() + str(num)
    calc.delete(0, tk.END)
    calc.insert(0, value)
def add_operation(operaation):
    value = calc.get()
    if value[-1] in '+-/***!':
        value = value[:-1]
    calc.delete(0, tk.END)
    calc.insert(0, value + operaation)
def nums_buttons(num):
    return tk.Button(text=num, bd=5, command= lambda: add_num(num))
def operation_buttons(operation):
    return tk.Button(text=operation, bd=5, command= lambda: add_operation(operation))
def calculate_button(operation):
    return tk.Button(text=operation, bd=5, command=calculate)
def clear_button(operation):
    return tk.Button(text=operation, bd=5, command=clear)
def calear_button():
    calc.delete(0, tk.END)
def press_key(press):
    if press.char.isdigit():
        add_num(press.char)
    elif press.char in '+-/**!':
        add_operation(press.char)
    elif press.char == '\r':
        calculate()
    elif press.char == '\x08':
        clear()
win = tk.Tk()
win.geometry(f'310x310')
win['bg'] = '#cadced'
win.title('Трыц Тыц Калькулятор и два фиксика внутри')
win.resizable(False, False)
win.bind('<Key>', press_key)
calc = tk.Entry(win, justify=tk.RIGHT, font=('Arial', 15))
calc.grid(row=0, column=0, columnspan=5, stick='we', padx=5)
nums_buttons(1).grid(row=1, column=0, sticky='wnes', padx=5, pady=5)
nums_buttons(2).grid(row=1, column=1, sticky='wnes', padx=5, pady=5)
nums_buttons(3).grid(row=1, column=2, sticky='wnes', padx=5, pady=5)
nums_buttons(4).grid(row=2, column=0, sticky='wnes', padx=5, pady=5)
nums_buttons(5).grid(row=2, column=1, sticky='wnes', padx=5, pady=5)
nums_buttons(6).grid(row=2, column=2, sticky='wnes', padx=5, pady=5)
nums_buttons(7).grid(row=3, column=0, sticky='wnes', padx=5, pady=5)
nums_buttons(8).grid(row=3, column=1, sticky='wnes', padx=5, pady=5)
nums_buttons(9).grid(row=3, column=2, sticky='wnes', padx=5, pady=5)
nums_buttons(0).grid(row=4, column=0, sticky='wnes', padx=5, pady=5)

operation_buttons('+').grid(row=1, column=3, sticky='wnes', padx=5, pady=5)
operation_buttons('-').grid(row=2, column=3, sticky='wnes', padx=5, pady=5)
operation_buttons('*').grid(row=3, column=3, sticky='wnes', padx=5, pady=5)
operation_buttons('/').grid(row=4, column=3, sticky='wnes', padx=5, pady=5)
calculate_button('=').grid(row=4, column=2, sticky='wnes', padx=5, pady=5)
clear_button('C').grid(row=4, column=1, sticky='wnes', padx=5, pady=5)
operation_buttons('**').grid(row=1, column=4, sticky='wnes', padx=5, pady=5)
operation_buttons('!').grid(row=2, column=4, sticky='wnes', padx=5, pady=5)

win.grid_columnconfigure(0, minsize=60)
win.grid_columnconfigure(1, minsize=60)
win.grid_columnconfigure(2, minsize=60)
win.grid_columnconfigure(3, minsize=60)
win.grid_columnconfigure(4, minsize=60)

win.grid_rowconfigure(0, minsize=60)
win.grid_rowconfigure(1, minsize=60)
win.grid_rowconfigure(2, minsize=60)
win.grid_rowconfigure(3, minsize=60)
win.grid_rowconfigure(4, minsize=60)

win.mainloop()
