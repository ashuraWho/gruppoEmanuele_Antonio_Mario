from datetime import datetime

class Studente(Person):
    def __init__(self, nome, data_nascita, matricola):
        super().__init__(nome, data_nascita)
        self.matricola = matricola

    def __str__(self):
        eta = datetime.now().year - self.data_nascita.year
        return f"{self.nome} - Matricola: {self.matricola} - Età: {eta} anni"
