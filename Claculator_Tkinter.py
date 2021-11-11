import math
from tkinter import *

root = Tk()
root.title("DEV's CALCULATOR")

input_field = Entry(root, bg="#9bd12e", fg="black", width=27, font=20, borderwidth=9, relief=SUNKEN)
input_field.grid(row=0, column=0, columnspan=5)
op = ""
var1 = 0


def display(number):
    input_field.insert(END, number)


def operation(operator):                 # FUNCTION WHEN ANY OPERATOR IS PRESS
    global var1, op
    op = operator
    var1 = float(input_field.get())
    input_field.delete(0, END)

    if "sqrt" in operator:
        input_field.insert(0, math.sqrt(var1))
        var1 = 0
    elif "square" in operator:
        input_field.insert(0, math.pow(var1, 2))
        var1 = 0
    elif "factorial" in operator:
        x = 1
        while var1 != 1:
            x *= var1
            var1 -= 1
        input_field.insert(0, x)
        var1 = 0


def equal():             # FUNCTION  WHEN EQUAL BUTTON IS PRESS
    global var1
    var2 = int(input_field.get())
    input_field.delete(0, END)
    if "+" in op:
        answer = var1 + var2
        input_field.insert(0, answer)
    elif "-" in op:
        answer = var1 - var2
        input_field.insert(0, answer)
    elif "*" in op:
        answer = var1 * var2
        input_field.insert(0, answer)
    elif "/" in op:
        answer = "{:.3f}".format(var1 / var2)
        input_field.insert(0, answer)
    var1 = 0


def clear():
    input_field.delete(0, END)


# DEFINING THE BUTTONS
Button_1 = Button(root, text="1", bg="#0a0d0a", fg="white", padx=20, pady=15, font="bold", command=lambda: display(1))
Button_2 = Button(root, text="2", bg="#0a0d0a", fg="white", padx=20, pady=15, font="bold", command=lambda: display(2))
Button_3 = Button(root, text="3", bg="#0a0d0a", fg="white", padx=20, pady=15, font="bold", command=lambda: display(3))
Button_4 = Button(root, text="4", bg="#0a0d0a", fg="white", padx=20, pady=15, font="bold", command=lambda: display(4))
Button_5 = Button(root, text="5", bg="#0a0d0a", fg="white", padx=20, pady=15, font="bold", command=lambda: display(5))
Button_6 = Button(root, text="6", bg="#0a0d0a", fg="white", padx=20, pady=15, font="bold", command=lambda: display(6))
Button_7 = Button(root, text="7", bg="#0a0d0a", fg="white", padx=20, pady=15, font="bold", command=lambda: display(7))
Button_8 = Button(root, text="8", bg="#0a0d0a", fg="white", padx=20, pady=15, font="bold", command=lambda: display(8))
Button_9 = Button(root, text="9", bg="#0a0d0a", fg="white", padx=20, pady=15, font="bold", command=lambda: display(9))
Button_0 = Button(root, text="0", bg="#0a0d0a", fg="white", padx=20, pady=15, font="bold", command=lambda: display(0))

Button_add = Button(root, text="+", bg="#14213d", fg="white", padx=20, pady=15, font="bold", command=lambda: operation("+"))
Button_sub = Button(root, text="-", bg="#14213d", fg="white", padx=22, pady=15, font="bold", command=lambda: operation("-"))
Button_mul = Button(root, text="", bg="#14213d", fg="white", padx=22, pady=15, font="bold", command=lambda: operation(""))
Button_divide = Button(root, text="/", bg="#14213d", fg="white", padx=23, pady=15, font="bold", command=lambda: operation("/"))
Button_sqrt = Button(root, text="√x", bg="#14213d", fg="white", padx=15, pady=15, font="bold", command=lambda: operation("sqrt"))
Button_square = Button(root, text="x²", bg="#14213d", fg="white", padx=18, pady=15, font="bold", command=lambda: operation("square"))
Button_factorial = Button(root, text="x!", bg="#14213d", fg="white", padx=19, pady=15, font="bold", command=lambda: operation("factorial"))

Button_equal = Button(root, text="=", bg="#b1b3ba", fg="black", padx=55, pady=15, font=30, command=lambda: equal())
Button_clear = Button(root, text="Clear", bg="#b1b3ba", fg="black", padx=140, pady=10, font=25, command=clear)

# PUTTING THINGS(Buttons) ON SCREEN WITH GRID LAYOUT
Button_1.grid(row=3, column=0)
Button_2.grid(row=3, column=1)
Button_3.grid(row=3, column=2)
Button_4.grid(row=2, column=0)
Button_5.grid(row=2, column=1)
Button_6.grid(row=2, column=2)
Button_7.grid(row=1, column=0)
Button_8.grid(row=1, column=1)
Button_9.grid(row=1, column=2)
Button_0.grid(row=4, column=0)

Button_add.grid(row=1, column=3)
Button_sub.grid(row=2, column=3)
Button_mul.grid(row=3, column=3)
Button_divide.grid(row=4, column=3)
Button_sqrt.grid(row=1, column=4)
Button_square.grid(row=2, column=4)
Button_factorial.grid(row=3, column=4)

Button_equal.grid(row=4, column=1, columnspan=2)
Button_clear.grid(row=5, column=0, columnspan=5)

root.mainloop()
