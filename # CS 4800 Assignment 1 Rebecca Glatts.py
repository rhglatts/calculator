# CS 4800 Assignment 1 Rebecca Glatts
import tkinter as tk
equation = ""
b_height = 8

def update_display(symbol):
    global equation
    if symbol != 0 or equation != 0:
        equation += symbol
    
    label.config(text=equation)

def clear_display():
    global equation
    equation = ""
    label.config(text=0)

def backspace_display():
    global equation
    equation = equation[1:]
    label.config(equation)

def calculate_equation():
    global equation
    label.config(text=eval(equation))
    equation = ""

# main window
calculator = tk.Tk()
calculator.geometry("600x800")
# display area for equation
display = tk.Frame(calculator, width=600, height=80) #bg="#fedad2"
display.grid(row=0, column=0)
label = tk.Label(display, text=0)
label.grid(row=0, column=0)


button_7 = tk.Button(text="7", height=b_height, width=15, command = lambda : update_display("7"))
button_7.grid(row=1, column=0)
button_8 = tk.Button(text="8", height=b_height, width=15, command = lambda : update_display("8"))
button_8.grid(row=1, column=1)
button_9 = tk.Button(text="9", height=b_height, width=15, command = lambda : update_display("9"))
button_9.grid(row=1, column=2)
button_divide = tk.Button(text="/", height=b_height, width=15, command = lambda : update_display("/"))
button_divide.grid(row=1, column=3)


button_4 = tk.Button(text="4", height=b_height, width=15, command = lambda : update_display("4"))
button_4.grid(row=2, column=0)
button_5 = tk.Button(text="5", height=b_height, width=15, command = lambda : update_display("5"))
button_5.grid(row=2, column=1)
button_6 = tk.Button(text="6", height=b_height, width=15, command = lambda : update_display("6"))
button_6.grid(row=2, column=2)
button_multiply = tk.Button(text="*", height=b_height, width=15, command = lambda : update_display("*"))
button_multiply.grid(row=2, column=3)

button_1 = tk.Button(text="1", height=b_height, width=15, command = lambda : update_display("1"))
button_1.grid(row=3, column=0)
button_2 = tk.Button(text="2", height=b_height, width=15, command = lambda : update_display("2"))
button_2.grid(row=3, column=1)
button_3 = tk.Button(text="3", height=b_height, width=15, command = lambda : update_display("3"))
button_3.grid(row=3, column=2)
button_minus = tk.Button(text="-", height=b_height, width=15, command = lambda : update_display("-"))
button_minus.grid(row=3, column=3)

button_0 = tk.Button(text="0", height=b_height, width=15, command = lambda : update_display("0"))
button_0.grid(row=4, column=0)
button_decimal = tk.Button(text=".", height=b_height, width=15, command = lambda : update_display("."))
button_decimal.grid(row=4, column=1)
button_equals = tk.Button(text="=", height=b_height, width=15, command = calculate_equation)
button_equals.grid(row=4, column=2)
button_add = tk.Button(text="+", height=b_height, width=15, command =  lambda : update_display("+"))
button_add.grid(row=4, column=3)


button_clear = tk.Button(text="Clear", height=b_height, width=15, command = clear_display)
button_clear.grid(row=5, column=0)
button_delete = tk.Button(text="Delete", height=b_height, width=15, command = backspace_display)
button_delete.grid(row=5, column=1)

calculator.mainloop()


