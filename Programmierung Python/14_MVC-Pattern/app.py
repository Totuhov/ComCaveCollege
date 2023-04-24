import view
import controller
import model

class App:
    def __init__(self):
        self.window = view.View()
        self.model = model.Model("example@email.com")

        self.window.setController(controller.Controller(self.model, self.window))

        self.window.mainloop()
       

if __name__ == "__main__":
    app = App()