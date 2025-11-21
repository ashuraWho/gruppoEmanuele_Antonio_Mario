from persona import Persona

class Professore(Persona): # Classe figlio di "Person" (per i Professori)
    def __init__(self, nome: str, eta: int, materia: str):
        super().__init__(nome)
        
        self.materia = materia # Professore