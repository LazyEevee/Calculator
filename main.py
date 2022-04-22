from tkinter import *


class Calculator:
    def __init__(self, main):
        self.var = IntVar()
        self.sym = "0"
        self.light = "#dedede"
        self.dark = "#212121"
        self.back_colour = self.light
        self.fore_colour = self.dark
        self.math = "clear"
        self.total = 0

        self.button_1 = Button(main, text="1", width=4, height=1, command=lambda: self.button_click(1),
                               font="Helvetica 18")
        self.button_2 = Button(main, text="2", width=4, height=1, command=lambda: self.button_click(2),
                               font="Helvetica 18")
        self.button_3 = Button(main, text="3", width=4, height=1, command=lambda: self.button_click(3),
                               font="Helvetica 18")
        self.button_4 = Button(main, text="4", width=4, height=1, command=lambda: self.button_click(4),
                               font="Helvetica 18")
        self.button_5 = Button(main, text="5", width=4, height=1, command=lambda: self.button_click(5),
                               font="Helvetica 18")
        self.button_6 = Button(main, text="6", width=4, height=1, command=lambda: self.button_click(6),
                               font="Helvetica 18")
        self.button_7 = Button(main, text="7", width=4, height=1, command=lambda: self.button_click(7),
                               font="Helvetica 18")
        self.button_8 = Button(main, text="8", width=4, height=1, command=lambda: self.button_click(8),
                               font="Helvetica 18")
        self.button_9 = Button(main, text="9", width=4, height=1, command=lambda: self.button_click(9),
                               font="Helvetica 18")
        self.button_0 = Button(main, text="0", width=4, height=1, command=lambda: self.button_click(0),
                               font="Helvetica 18")
        self.button_equal = Button(main, text="=", width=4, height=1, command=lambda: self.button_calc("="),
                                   font="Helvetica 18")
        self.btn_clear = Button(main, text="AC", width=4, height=1, command=self.button_clear, font="Helvetica 18")
        self.button_add = Button(main, text="+", width=4, height=1, command=lambda: self.button_calc("+"),
                                 font="Helvetica 18")
        self.button_subtract = Button(main, text="-", width=4, height=1, command=lambda: self.button_calc("-"),
                                      font="Helvetica 18")
        self.button_multiply = Button(main, text="*", width=4, height=1, command=lambda: self.button_calc("*"),
                                      font="Helvetica 18")
        self.button_divide = Button(main, text="/", width=4, height=1, command=lambda: self.button_calc("/"),
                                    font="Helvetica 18")

        self.dark_mode = Checkbutton(main, text="Dark Mode", variable=self.var, command=self.colour)
        self.dark_mode.deselect()

        self.entry = Entry(main, width=18, borderwidth=5, justify="right", font="Helvetica 18")
        self.dark_mode.grid(row=0, column=1, columnspan=2)
        self.entry.grid(row=1, column=0, columnspan=5, padx=0, pady=5)
        self.button_7.grid(row=2, column=0)
        self.button_8.grid(row=2, column=1)
        self.button_9.grid(row=2, column=2)
        self.button_divide.grid(row=2, column=3)
        self.button_4.grid(row=3, column=0)
        self.button_5.grid(row=3, column=1)
        self.button_6.grid(row=3, column=2)
        self.button_multiply.grid(row=3, column=3)
        self.button_1.grid(row=4, column=0)
        self.button_2.grid(row=4, column=1)
        self.button_3.grid(row=4, column=2)
        self.button_subtract.grid(row=4, column=3)
        self.btn_clear.grid(row=5, column=0)
        self.button_0.grid(row=5, column=1)
        self.button_equal.grid(row=5, column=2)
        self.button_add.grid(row=5, column=3)

        self.entry.insert(0, "0")

        root.config(bg=self.back_colour)
        self.dark_mode.config(bg=self.back_colour, fg=self.fore_colour, selectcolor=self.back_colour,
                              activebackground=self.back_colour, activeforeground=self.fore_colour)
        self.entry.config(bg=self.back_colour, fg=self.fore_colour)
        self.button_1.config(bg=self.back_colour, fg=self.fore_colour)
        self.button_2.config(bg=self.back_colour, fg=self.fore_colour)
        self.button_3.config(bg=self.back_colour, fg=self.fore_colour)
        self.button_4.config(bg=self.back_colour, fg=self.fore_colour)
        self.button_5.config(bg=self.back_colour, fg=self.fore_colour)
        self.button_6.config(bg=self.back_colour, fg=self.fore_colour)
        self.button_7.config(bg=self.back_colour, fg=self.fore_colour)
        self.button_8.config(bg=self.back_colour, fg=self.fore_colour)
        self.button_9.config(bg=self.back_colour, fg=self.fore_colour)
        self.btn_clear.config(bg=self.back_colour, fg=self.fore_colour)
        self.button_0.config(bg=self.back_colour, fg=self.fore_colour)
        self.button_equal.config(bg=self.back_colour, fg=self.fore_colour)
        self.button_add.config(bg=self.back_colour, fg=self.fore_colour)
        self.button_subtract.config(bg=self.back_colour, fg=self.fore_colour)
        self.button_multiply.config(bg=self.back_colour, fg=self.fore_colour)
        self.button_divide.config(bg=self.back_colour, fg=self.fore_colour)

    def colour(self):
        mode = str(self.var.get())
        if mode == "0":
            self.back_colour = self.light
            self.fore_colour = self.dark
        elif mode == "1":
            self.back_colour = self.dark
            self.fore_colour = self.light
        root.config(bg=self.back_colour)
        self.dark_mode.config(bg=self.back_colour, fg=self.fore_colour, selectcolor=self.back_colour,
                              activebackground=self.back_colour, activeforeground=self.fore_colour)
        self.entry.config(bg=self.back_colour, fg=self.fore_colour)
        self.button_1.config(bg=self.back_colour, fg=self.fore_colour)
        self.button_2.config(bg=self.back_colour, fg=self.fore_colour)
        self.button_3.config(bg=self.back_colour, fg=self.fore_colour)
        self.button_4.config(bg=self.back_colour, fg=self.fore_colour)
        self.button_5.config(bg=self.back_colour, fg=self.fore_colour)
        self.button_6.config(bg=self.back_colour, fg=self.fore_colour)
        self.button_7.config(bg=self.back_colour, fg=self.fore_colour)
        self.button_8.config(bg=self.back_colour, fg=self.fore_colour)
        self.button_9.config(bg=self.back_colour, fg=self.fore_colour)
        self.btn_clear.config(bg=self.back_colour, fg=self.fore_colour)
        self.button_0.config(bg=self.back_colour, fg=self.fore_colour)
        self.button_equal.config(bg=self.back_colour, fg=self.fore_colour)
        self.button_add.config(bg=self.back_colour, fg=self.fore_colour)
        self.button_subtract.config(bg=self.back_colour, fg=self.fore_colour)
        self.button_multiply.config(bg=self.back_colour, fg=self.fore_colour)
        self.button_divide.config(bg=self.back_colour, fg=self.fore_colour)

    def button_click(self, number):
        if self.math == "equal":
            self.entry.delete(0, END)
            self.math = "clear"
        if self.entry.get() == "0":
            self.entry.delete(0, END)
        local = self.entry.get()
        self.entry.delete(0, END)
        self.entry.insert(0, local + str(number))

    def button_clear(self):
        self.entry.delete(0, END)
        self.entry.insert(0, "0")
        self.total = 0
        self.math = "clear"

    def button_calc(self, sym):
        # get value in entry box
        current = int(self.entry.get())
        # clear entry box
        self.entry.delete(0, END)
        # check which math function was used previously and change total accordingly
        if self.math == "add":
            self.total = self.total + current
        elif self.math == "subtract":
            self.total = self.total - current
        elif self.math == "multiply":
            self.total = self.total * current
        elif self.math == "divide":
            self.total = self.total / current
        else:
            self.total = current

        # check if equals pressed and reset total after total value shown
        if sym == "=":
            self.math = "equal"
            self.entry.insert(0, str(self.total))
            self.total = 0

        # change math value to button pressed on this function call
        elif sym == "+":
            self.math = "add"
        elif sym == "-":
            self.math = "subtract"
        elif sym == "*":
            self.math = "multiply"
        elif sym == "/":
            self.math = "divide"


if __name__ == "__main__":
    root = Tk()
    root.title("Simple Calculator")
    root.iconbitmap('images/calc.ico')
    app = Calculator(root)
    root.mainloop()
