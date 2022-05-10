from tkinter import *
from math import sqrt


class Calculator:
    def __init__(self, main):
        # initialise class values
        self.main = None
        self.var = IntVar()
        self.sym = "0"
        self.light = "#dedede"
        self.dark = "#212121"
        self.back_colour = self.light
        self.fore_colour = self.dark
        self.math = "clear"
        self.total = 0

        # set background colour
        root.config(bg=self.back_colour)

        # dark mode checkbutton
        self.dark_mode = Checkbutton(main, text="Dark Mode", variable=self.var, command=self.colour)
        self.dark_mode.grid(row=0, column=1, columnspan=2)
        self.dark_mode.deselect()
        self.dark_mode.config(bg=self.back_colour, fg=self.fore_colour, selectcolor=self.back_colour,
                              activebackground=self.back_colour, activeforeground=self.fore_colour)

        # entry box
        self.entry = Entry(main, width=18, borderwidth=5, justify="right", font="Helvetica 18")
        self.entry.grid(row=1, column=0, columnspan=5, padx=0, pady=5)
        self.entry.insert(0, "0")
        self.entry.config(bg=self.back_colour, fg=self.fore_colour)

        # buttons in order of grid
        self.buttons = ["AC", "√", "", "/",
                        "7", "8", "9", "*",
                        "4", "5", "6", "-",
                        "1", "2", "3", "+",
                        "+/-", "0", ".", "="]

        self.draw_buttons(self.buttons)

    def draw_buttons(self, buttons):
        # loop over required buttons
        i = 0
        for c in buttons:
            button = Button(self.main, text=c, width=4, height=1,
                            bg=self.back_colour, fg=self.fore_colour,
                            font="Helvetica 18")
            button.grid(row=int(i / 4) + 2, column=(i % 4))
            # add command depending on which button drawn
            if c in ("1", "2", "3", "4", "5", "6", "7", "8", "9", "0", "."):
                button.config(command=lambda b=c: self.button_click(b))
            elif c == "+/-":
                button.config(command=self.negative_positive)
            elif c == "AC":
                button.config(command=self.button_clear)
            elif c == "√":
                button.config(command=self.square_root)
            elif c == "":
                button.config(state=DISABLED)
            else:
                button.config(command=lambda b=c: self.button_calc(b))
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
        self.draw_buttons(self.buttons)

    def button_click(self, number):
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

    def button_clear(self):
        # clear the entry box
        self.entry.delete(0, END)
        # insert a 0 into entry box
        self.entry.insert(0, "0")
        # set running total to 0
        self.total = 0
        # set math to clear
        self.math = "clear"

    def negative_positive(self):
        # get input and convert to float
        local = float(self.entry.get())
        # clear input so new input can be shown
        self.entry.delete(0, END)
        # check if input is int or float to neaten up
        if local.is_integer():
            local = int(local)
        else:
            local = local
        # check if input is currently positive or negative, then change to other
        if local > 0:
            self.entry.insert(0, "-" + str(local))
        elif local < 0:
            self.entry.insert(0, str(local*-1))
        else:
            self.entry.insert(0, str(local))

    def square_root(self):
        # get number in entry box
        current = float(self.entry.get())
        # clear entry box
        self.entry.delete(0, END)
        result = sqrt(current)
        # convert float to int if needed
        if result.is_integer():
            result = int(result)
        # insert answer to entry
        self.entry.insert(0, str(result))
        # set math to equal for future calculations
        self.math = "equal"

    def button_calc(self, sym):
        # get value in entry box
        current = float(self.entry.get())
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
            total = self.total
            # convert float to int if needed
            if total.is_integer():
                total = int(total)
            self.entry.insert(0, str(total))
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
