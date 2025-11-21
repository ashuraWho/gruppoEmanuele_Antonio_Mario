"""
    
    Implemento tutta la logica per definire una persona:
        - studenti
        - professori
    
"""

class Persona: # Classe base
    def __init__(self, nome: str, data_nascita: str):
        self._nome = nome
        self._data_nascita = data_nascita
    
    def info(self):
        return f"Nome: {self.nome} (data di nascita: {self.data_nascita})"