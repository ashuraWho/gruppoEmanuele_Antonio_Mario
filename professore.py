from persona import Person as Persona

class Professore(Persona): # Classe figlio di "Person" (per i Professori)
    def __init__(self, nome: str, data_nascita: str, materia: str):
        super().__init__(nome, data_nascita)
        
        self.materia = materia # Professore
        
    def presentazione(self) -> str:
        return f"nome: {self._nome}, età: {self._eta}, materia: {self.materia}"