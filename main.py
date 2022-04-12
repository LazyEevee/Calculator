from tkinter import *

root = Tk()
root.title("Simple Calculator")
root.iconbitmap('images/calc.ico')

entry = Entry(root, width=40, borderwidth=5, justify="right")
entry.grid(row=0, column=0, columnspan=5, padx=5, pady=5)


def button_click(number):
    current = entry.get()
    entry.delete(0, END)
    entry.insert(0, current + str(number))


def button_clear():
    entry.delete(0, END)


def button_add():
    first_num = entry.get()
    global f_num
    global math
    math = "addition"
    f_num = int(first_num)
    entry.delete(0, END)


def button_equal():
    second_num = entry.get()
    entry.delete(0, END)
    if math == "addition":
        entry.insert(0, f_num + int(second_num))
    if math == "subtraction":
        entry.insert(0, f_num - int(second_num))
    if math == "multiplication":
        entry.insert(0, f_num * int(second_num))
    if math == "division":
        entry.insert(0, f_num / int(second_num))


def button_subtract():
    first_num = entry.get()
    global f_num
    global math
    math = "subtraction"
    f_num = int(first_num)
    entry.delete(0, END)


def button_multiply():
    first_num = entry.get()
    global f_num
    global math
    math = "multiplication"
    f_num = int(first_num)
    entry.delete(0, END)


def button_divide():
    first_num = entry.get()
    global f_num
    global math
    math = "division"
    f_num = int(first_num)
    entry.delete(0, END)


button_1 = Button(root, text="1", width=10, height=3, command=lambda: button_click(1))
button_2 = Button(root, text="2", width=10, height=3, command=lambda: button_click(2))
button_3 = Button(root, text="3", width=10, height=3, command=lambda: button_click(3))
button_4 = Button(root, text="4", width=10, height=3, command=lambda: button_click(4))
button_5 = Button(root, text="5", width=10, height=3, command=lambda: button_click(5))
button_6 = Button(root, text="6", width=10, height=3, command=lambda: button_click(6))
button_7 = Button(root, text="7", width=10, height=3, command=lambda: button_click(7))
button_8 = Button(root, text="8", width=10, height=3, command=lambda: button_click(8))
button_9 = Button(root, text="9", width=10, height=3, command=lambda: button_click(9))
button_0 = Button(root, text="0", width=10, height=3, command=lambda: button_click(0))

button_equal = Button(root, text="=", width=10, height=3, command=button_equal)
button_clear = Button(root, text="Clear", width=10, height=3, command=button_clear)

button_add = Button(root, text="+", width=10, height=3, command=button_add)
button_subtract = Button(root, text="-", width=10, height=3, command=button_subtract)
button_multiply = Button(root, text="*", width=10, height=3, command=button_multiply)
button_divide = Button(root, text="/", width=10, height=3, command=button_divide)

button_1.grid(row=3, column=0)
button_2.grid(row=3, column=1)
button_3.grid(row=3, column=2)

button_4.grid(row=2, column=0)
button_5.grid(row=2, column=1)
button_6.grid(row=2, column=2)

button_7.grid(row=1, column=0)
button_8.grid(row=1, column=1)
button_9.grid(row=1, column=2)

button_clear.grid(row=4, column=0)
button_0.grid(row=4, column=1)
button_equal.grid(row=4, column=2)

button_add.grid(row=1, column=4)
button_subtract.grid(row=2, column=4)
button_multiply.grid(row=3, column=4)
button_divide.grid(row=4, column=4)

# event loop
root.mainloop()
