from tkinter import *

light = "#dedede"
dark = "#212121"
back_colour = light
fore_colour = dark

root = Tk()
root.title("Simple Calculator")
root.iconbitmap('images/calc.ico')

options_frame = Frame(root)
entry_frame = Frame(root)
main_frame = Frame(root)

options_frame.grid(row=0, column=0)
entry_frame.grid(row=1, column=0)
main_frame.grid(row=2, column=0)


def colour():
    global back_colour
    global fore_colour
    mode = var.get()
    if mode == "Light Mode":
        back_colour = light
        fore_colour = dark
    elif mode == "Dark Mode":
        back_colour = dark
        fore_colour = light
    root.config(bg=back_colour)
    options_frame.config(bg=back_colour)
    entry_frame.config(bg=back_colour)
    main_frame.config(bg=back_colour)
    dark_mode.config(bg=back_colour, fg=fore_colour, selectcolor=back_colour, activebackground=back_colour,
                     activeforeground=fore_colour)
    apply.config(bg=back_colour, fg=fore_colour, activebackground=back_colour, activeforeground=fore_colour)
    entry.config(bg=back_colour, fg=fore_colour)
    button_1.config(bg=back_colour, fg=fore_colour)
    button_2.config(bg=back_colour, fg=fore_colour)
    button_3.config(bg=back_colour, fg=fore_colour)
    button_4.config(bg=back_colour, fg=fore_colour)
    button_5.config(bg=back_colour, fg=fore_colour)
    button_6.config(bg=back_colour, fg=fore_colour)
    button_7.config(bg=back_colour, fg=fore_colour)
    button_8.config(bg=back_colour, fg=fore_colour)
    button_9.config(bg=back_colour, fg=fore_colour)
    button_clear.config(bg=back_colour, fg=fore_colour)
    button_0.config(bg=back_colour, fg=fore_colour)
    button_equal.config(bg=back_colour, fg=fore_colour)
    button_add.config(bg=back_colour, fg=fore_colour)
    button_subtract.config(bg=back_colour, fg=fore_colour)
    button_multiply.config(bg=back_colour, fg=fore_colour)
    button_divide.config(bg=back_colour, fg=fore_colour)


var = StringVar()
dark_mode = Checkbutton(options_frame, text="Dark Mode", variable=var, onvalue="Dark Mode", offvalue="Light Mode")
dark_mode.deselect()
dark_mode.grid(row=0, column=0)
apply = Button(options_frame, text="Apply", command=colour)
apply.grid(row=0, column=1)

entry = Entry(entry_frame, width=18, borderwidth=5, justify="right", font="Helvetica 18")
entry.grid(row=0, column=0, columnspan=5, padx=0, pady=5)
entry.insert(0, "0")

# global variables
math = "clear"
total = 0


def button_click(number):
    global math

    if math == "equal":
        entry.delete(0, END)
        math = "clear"
    if entry.get() == "0":
        entry.delete(0, END)
    local = entry.get()
    entry.delete(0, END)
    entry.insert(0, local + str(number))


def button_clear():
    global total
    global math
    entry.delete(0, END)
    entry.insert(0, "0")
    total = 0
    math = "clear"


def button_calc(sym):
    global total
    global math

    # get value in entry box
    current = int(entry.get())
    # clear entry box
    entry.delete(0, END)
    # check which math function was used previously and change total accordingly
    if math == "add":
        total = total + current
    elif math == "subtract":
        total = total - current
    elif math == "multiply":
        total = total * current
    elif math == "divide":
        total = total / current
    else:
        total = current

    # check if equals pressed and reset total after total value shown
    if sym == "=":
        math = "equal"
        entry.insert(0, str(total))
        total = 0

    # change math value to button pressed on this function call
    elif sym == "+":
        math = "add"
    elif sym == "-":
        math = "subtract"
    elif sym == "*":
        math = "multiply"
    elif sym == "/":
        math = "divide"


button_1 = Button(main_frame, text="1", width=4, height=1, command=lambda: button_click(1), font="Helvetica 18")
button_2 = Button(main_frame, text="2", width=4, height=1, command=lambda: button_click(2), font="Helvetica 18")
button_3 = Button(main_frame, text="3", width=4, height=1, command=lambda: button_click(3), font="Helvetica 18")
button_4 = Button(main_frame, text="4", width=4, height=1, command=lambda: button_click(4), font="Helvetica 18")
button_5 = Button(main_frame, text="5", width=4, height=1, command=lambda: button_click(5), font="Helvetica 18")
button_6 = Button(main_frame, text="6", width=4, height=1, command=lambda: button_click(6), font="Helvetica 18")
button_7 = Button(main_frame, text="7", width=4, height=1, command=lambda: button_click(7), font="Helvetica 18")
button_8 = Button(main_frame, text="8", width=4, height=1, command=lambda: button_click(8), font="Helvetica 18")
button_9 = Button(main_frame, text="9", width=4, height=1, command=lambda: button_click(9), font="Helvetica 18")
button_0 = Button(main_frame, text="0", width=4, height=1, command=lambda: button_click(0), font="Helvetica 18")

button_equal = Button(main_frame, text="=", width=4, height=1, command=lambda: button_calc("="), font="Helvetica 18")
button_clear = Button(main_frame, text="AC", width=4, height=1, command=button_clear, font="Helvetica 18")

button_add = Button(main_frame, text="+", width=4, height=1, command=lambda: button_calc("+"), font="Helvetica 18")
button_subtract = Button(main_frame, text="-", width=4, height=1, command=lambda: button_calc("-"), font="Helvetica 18")
button_multiply = Button(main_frame, text="*", width=4, height=1, command=lambda: button_calc("*"), font="Helvetica 18")
button_divide = Button(main_frame, text="/", width=4, height=1, command=lambda: button_calc("/"), font="Helvetica 18")

button_1.grid(row=2, column=0)
button_2.grid(row=2, column=1)
button_3.grid(row=2, column=2)

button_4.grid(row=1, column=0)
button_5.grid(row=1, column=1)
button_6.grid(row=1, column=2)

button_7.grid(row=0, column=0)
button_8.grid(row=0, column=1)
button_9.grid(row=0, column=2)

button_clear.grid(row=3, column=0)
button_0.grid(row=3, column=1)
button_equal.grid(row=3, column=2)

button_add.grid(row=0, column=4)
button_subtract.grid(row=1, column=4)
button_multiply.grid(row=2, column=4)
button_divide.grid(row=3, column=4)

root.config(bg=back_colour)
root.config(bg=back_colour)
options_frame.config(bg=back_colour)
entry_frame.config(bg=back_colour)
main_frame.config(bg=back_colour)
dark_mode.config(bg=back_colour, fg=fore_colour, selectcolor=back_colour, activebackground=back_colour,
                 activeforeground=fore_colour)
apply.config(bg=back_colour, fg=fore_colour, activebackground=back_colour, activeforeground=fore_colour)
entry.config(bg=back_colour, fg=fore_colour)
button_1.config(bg=back_colour, fg=fore_colour)
button_2.config(bg=back_colour, fg=fore_colour)
button_3.config(bg=back_colour, fg=fore_colour)
button_4.config(bg=back_colour, fg=fore_colour)
button_5.config(bg=back_colour, fg=fore_colour)
button_6.config(bg=back_colour, fg=fore_colour)
button_7.config(bg=back_colour, fg=fore_colour)
button_8.config(bg=back_colour, fg=fore_colour)
button_9.config(bg=back_colour, fg=fore_colour)
button_clear.config(bg=back_colour, fg=fore_colour)
button_0.config(bg=back_colour, fg=fore_colour)
button_equal.config(bg=back_colour, fg=fore_colour)
button_add.config(bg=back_colour, fg=fore_colour)
button_subtract.config(bg=back_colour, fg=fore_colour)
button_multiply.config(bg=back_colour, fg=fore_colour)
button_divide.config(bg=back_colour, fg=fore_colour)

# event loop
root.mainloop()
