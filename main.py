from tkinter import *
from math import sqrt, pow


class Calculator:
    def __init__(self, main):
        # initialise class values
        self.main = None
        self.var = IntVar()
        self.sym = "0"
        self.light = "#dedede"  # light grey
        self.dark = "#212121"  # nearly black
        self.back_colour = self.light
        self.fore_colour = self.dark
        self.math = "clear"
        self.total = 0.0
        self.memory = 0.0

        # set background colour
        root.config(bg=self.back_colour)

        # dark mode checkbutton
        self.dark_mode = Checkbutton(main, text="Dark Mode", variable=self.var, command=self.colour)
        self.dark_mode.grid(row=0, column=0, columnspan=5)
        self.dark_mode.deselect()
        self.dark_mode.config(bg=self.back_colour, fg=self.fore_colour, selectcolor=self.back_colour,
                              activebackground=self.back_colour, activeforeground=self.fore_colour)

        # entry box
        self.entry = Entry(main, width=23, borderwidth=5, justify="right", font="Helvetica 18")
        self.entry.grid(row=1, column=0, columnspan=5, padx=0, pady=5)
        self.entry.insert(0, "0")
        self.entry.config(bg=self.back_colour, fg=self.fore_colour)

        # buttons in order of grid
        self.buttons = ["AC", "√x", "x²", "%", "/",
                        "CM", "7", "8", "9", "*",
                        "M+", "4", "5", "6", "-",
                        "M-", "1", "2", "3", "+",
                        "RM", "+/-", "0", ".", "="]

        self.draw_buttons()

    def draw_buttons(self):
        # loop over required buttons
        i = 0
        for c in self.buttons:
            button = Button(root, text=c, width=4, height=1,
                            bg=self.back_colour, fg=self.fore_colour,
                            font="Helvetica 18")
            button.grid(row=int(i / 5) + 2, column=(i % 5))
            # add command depending on which button drawn
            if c in ("1", "2", "3", "4", "5", "6", "7", "8", "9", "0", "."):
                button.config(command=lambda b=c: self.num(b))
            elif c == "+/-":
                button.config(command=self.negative_positive)
            elif c == "AC":
                button.config(command=self.clear)
            elif c == "√x":
                button.config(command=self.square_root)
            elif c == "x²":
                button.config(command=self.squared)
            elif c in ("CM", "M+", "M-", "RM"):
                button.config(command=lambda b=c: self.memory_func(b))
            elif c == "%":
                button.config(command=self.percentage)
            elif c == "=":
                button.config(command=self.equal)
            elif c in ("+", "-", "*", "/"):
                button.config(command=lambda b=c: self.calc(b))
            else:
                button.config(state=DISABLED)
            i += 1

    def colour(self):
        # get colour mode from checkbutton
        mode = str(self.var.get())
        # if mode is "0" change to light mode
        if mode == "0":
            self.back_colour = self.light
            self.fore_colour = self.dark
        # if mode is "1" change to dark mode
        elif mode == "1":
            self.back_colour = self.dark
            self.fore_colour = self.light
        # reconfig colours
        root.config(bg=self.back_colour)
        self.dark_mode.config(bg=self.back_colour, fg=self.fore_colour, selectcolor=self.back_colour,
                              activebackground=self.back_colour, activeforeground=self.fore_colour)
        self.entry.config(bg=self.back_colour, fg=self.fore_colour)
        # re-draw buttons
        self.draw_buttons()

    def num(self, number):
        # check for previous calculations
        # if equal clear previous answer
        if self.math == "equal":
            self.entry.delete(0, END)
            self.math = "clear"
        # if 0 clear number from entry
        if self.entry.get() == "0":
            self.entry.delete(0, END)
        # get current entry
        local = self.entry.get()
        # clear current entry
        self.entry.delete(0, END)
        # add button pressed to end of number
        self.entry.insert(0, local + str(number))
        return self.math

    def reset_total(self):
        self.total = 0
        return self.total

    def clear(self):
        # clear the entry box
        self.entry.delete(0, END)
        # insert a 0 into entry box
        self.entry.insert(0, "0")
        # set running total to 0
        self.reset_total()
        # set math to clear
        self.math = "clear"
        return self.math

    def negative_positive(self):
        # get input and convert to float
        local = float(self.entry.get())
        # clear input so new input can be shown
        self.entry.delete(0, END)
        # check if input is int or float to neaten up
        if local.is_integer():
            local = int(local)
        # check if input is currently positive or negative, then change to other
        if local > 0:
            self.entry.insert(0, "-" + str(local))
        elif local < 0:
            self.entry.insert(0, str(local*-1))
        else:
            self.entry.insert(0, str(local))

    def square_root(self):
        # get number in entry box
        local = float(self.entry.get())
        # clear entry box
        self.entry.delete(0, END)
        result = sqrt(local)
        # convert float to int if needed
        if result.is_integer():
            result = int(result)
        # insert answer to entry
        self.entry.insert(0, str(result))
        # set math to equal for future calculations
        self.math = "equal"
        return self.math

    def squared(self):
        # get number in entry box
        local = float(self.entry.get())
        # clear entry box
        self.entry.delete(0, END)
        result = pow(local, 2)
        # convert float to int if needed
        if result.is_integer():
            result = int(result)
        # insert answer to entry
        self.entry.insert(0, str(result))
        # set math to equal for future calculations
        self.math = "equal"
        return self.math

    def calc(self, sym):
        # get value in entry box
        local = float(self.entry.get())
        self.math_state(local)
        # clear entry box
        self.entry.delete(0, END)
        # change math value to button pressed on this function call
        if sym == "+":
            self.math = "add"
        elif sym == "-":
            self.math = "subtract"
        elif sym == "*":
            self.math = "multiply"
        elif sym == "/":
            self.math = "divide"
        return self.math

    def memory_func(self, func):
        if func == "RM":
            self.entry.delete(0, END)
            local = self.memory
            # convert float to int if needed
            if local.is_integer():
                local = int(local)
            self.entry.insert(0, str(local))
        if func == "CM":
            self.entry.delete(0, END)
            self.memory = 0.0
        if func == "M+":
            self.memory += float(self.entry.get())
        if func == "M-":
            self.memory -= float(self.entry.get())

    def math_state(self, local):
        # check which math function was used previously and change total accordingly
        if self.math == "add":
            self.total = self.total + local
        elif self.math == "subtract":
            self.total = self.total - local
        elif self.math == "multiply":
            self.total = self.total * local
        elif self.math == "divide":
            self.total = self.total / local
        else:
            self.total = local
        return self.total

    def equal(self):
        # get value in entry box
        local = float(self.entry.get())
        self.math_state(local)
        # clear entry box
        self.entry.delete(0, END)
        # convert float to int if needed
        if self.total.is_integer():
            self.total = int(self.total)
        self.entry.insert(0, str(self.total))
        self.reset_total()
        self.math = "equal"
        return self.math

    def percentage(self):
        # get value in entry box
        local = float(self.entry.get())
        # clear entry box
        self.entry.delete(0, END)
        # check which math function was used previously and change total accordingly
        local = (local / 100)
        if self.math == "add":
            self.total = self.total + (self.total * local)
        elif self.math == "subtract":
            self.total = self.total - (self.total * local)
        elif self.math == "multiply":
            self.total = self.total * local
        elif self.math == "divide":
            self.total = self.total / local
        else:
            self.total = local

        # convert float to int if needed
        if self.total.is_integer():
            self.total = int(self.total)
        self.entry.insert(0, str(self.total))
        self.math = "percent"
        return self.math


if __name__ == "__main__":
    root = Tk()
    root.title("Simple Calculator")
    root.iconbitmap('images/calc.ico')
    app = Calculator(root)
    root.mainloop()
