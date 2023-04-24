import model
import view

class Controller:
    def __init__(self, model:model.Model, view:view.View):
        self.model = model
        self.view = view

    def save(self, email):
        try:
            self.model.email = email
            self.model.save()

            self.view.showSuccess(f'Die Emaill -{email} - wurde gespeichert.')

        except ValueError as error:
            self.view.showError(error)