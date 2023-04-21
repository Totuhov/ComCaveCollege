import calculator_window as calculator
import convertor_window as convertor

class App():
    def __init__(self):
        self.window = calculator.CalculatorWindow()
        self.window.mainloop()  

    def switch_to_convertor(self, x, y):
        self.window = convertor.ConvertorWindow()
        self.window.geometry(f"330x450+{x}+{y}")
        self.window.mainloop()

    def switch_to_calculator(self, x, y):
        self.window = calculator.CalculatorWindow()
        self.window.geometry(f"330x450+{x}+{y}")
        self.window.mainloop()



# Echter Start für OOP-Applikation in Python
if __name__ == "__main__":
    app = App()