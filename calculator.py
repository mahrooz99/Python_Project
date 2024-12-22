import tkinter as tk
from math import sqrt, sin, cos, tan, radians


class AdvancedCalculator:
    def __init__(self, root):
        self.root = root
        self.root.title("Advanced Calculator")
        self.root.geometry("400x600")
        self.root.resizable(False, False)
        self.expression = ""
        self.result_var = tk.StringVar()

        # Entry widget
        self.entry = tk.Entry(root, textvariable=self.result_var, font=("Arial", 24), bd=10, insertwidth=2, width=14,
                              borderwidth=4, relief="ridge", justify='right')
        self.entry.grid(row=0, column=0, columnspan=4)

        # Buttons
        self.create_buttons()

    def create_buttons(self):
        buttons = [
            '7', '8', '9', '/',
            '4', '5', '6', '*',
            '1', '2', '3', '-',
            'C', '0', '=', '+',
            'sqrt', '^', 'sin',
            'cos', 'tan'
        ]

        row = 1
        col = 0

        for button in buttons:
            action = lambda x=button: self.button_click(x)
            b = tk.Button(self.root, text=button, padx=20, pady=20, font=("Arial", 14), command=action)
            b.grid(row=row, column=col, sticky="nsew")

            col += 1
            if col > 3:
                col = 0
                row += 1

        # Adjust column weights for better layout
        for i in range(4):
            self.root.grid_columnconfigure(i, weight=1)

    def button_click(self, button):
        if button == "C":
            self.expression = ""
            self.result_var.set("")
        elif button == "=":
            try:
                self.expression = self.expression.replace('^', '**')
                result = eval(self.expression)
                self.result_var.set(result)
                self.expression = str(result)
            except Exception as e:
                self.result_var.set("Error")
                self.expression = ""
        elif button in ['sqrt', 'sin', 'cos', 'tan']:
            try:
                if button == 'sqrt':
                    result = sqrt(float(self.expression))
                elif button == 'sin':
                    result = sin(radians(float(self.expression)))
                elif button == 'cos':
                    result = cos(radians(float(self.expression)))
                elif button == 'tan':
                    result = tan(radians(float(self.expression)))

                self.result_var.set(result)
                self.expression = str(result)
            except Exception as e:
                self.result_var.set("Error")
                self.expression = ""
        else:
            self.expression += button
            self.result_var.set(self.expression)


if __name__ == "__main__":
    root = tk.Tk()
    calc = AdvancedCalculator(root)
    root.mainloop()
