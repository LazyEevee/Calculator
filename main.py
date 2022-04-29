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

        self.dark_mode = Checkbutton(main, text="Dark Mode", variable=self.var, command=self.colour)
        self.dark_mode.deselect()

        self.entry = Entry(main, width=18, borderwidth=5, justify="right", font="Helvetica 18")
        self.dark_mode.grid(row=0, column=1, columnspan=2)
        self.entry.grid(row=1, column=0, columnspan=5, padx=0, pady=5)
        self.entry.insert(0, "0")

        root.config(bg=self.back_colour)
        self.dark_mode.config(bg=self.back_colour, fg=self.fore_colour, selectcolor=self.back_colour,
                              activebackground=self.back_colour, activeforeground=self.fore_colour)
        self.entry.config(bg=self.back_colour, fg=self.fore_colour)

        self.buttons = ["7", "8", "9", "/", "4", "5", "6", "*", "1", "2", "3", "-", "AC", "0", "=", "+"]
        i = 0
        for c in self.buttons:
            button = Button(main, text=c, width=4, height=1,
                            bg=self.back_colour, fg=self.fore_colour,
                            font="Helvetica 18")
            button.grid(row=int(i / 4)+2, column=(i % 4))

            if c in ("1", "2", "3", "4", "5", "6", "7", "8", "9", "0"):
                button.config(command=lambda b=c: self.button_click(b))
            elif c == "AC":
                button.config(command=self.button_clear)
            else:
                button.config(command=lambda b=c: self.button_calc(b))
            i += 1

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

        i = 0
        for c in self.buttons:
            button = Button(text=c, width=4, height=1,
                            bg=self.back_colour, fg=self.fore_colour,
                            font="Helvetica 18")
            button.grid(row=int(i / 4) + 2, column=(i % 4))

            if c in ("1", "2", "3", "4", "5", "6", "7", "8", "9", "0"):
                button.config(command=lambda b=c: self.button_click(b))
            elif c == "AC":
                button.config(command=self.button_clear)
            else:
                button.config(command=lambda b=c: self.button_calc(b))
            i += 1

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
