import re

class Model:
    def __init__(self, email):
        self.email = email

    @property
    def email(self):
        return self.__email
    
    @email.setter
    def email(self, value):
        "Validieren der E-Mail  zeichen@zeichen.2zeichen"
        pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'

        if re.fullmatch(pattern, value):
            self.__email = value
        else:
            raise ValueError(f'Invalid email adress: {value}')
        
    def save(self):
        with open('emails.txt', 'a') as f:
            f.write(self.email + '\n')
