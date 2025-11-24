"""
    
    Implemento tutta la logica per definire una persona:
        - studenti
        - professori
    
"""

class Persona: # Classe base
    def __init__(self, nome: str, data_nascita: str):
        self._nome = nome
        self._data_nascita = data_nascita
    
    @property
    def nome(self):
        return self._nome
    
    @property
    def data_nascita(self):
        return self._data_nascita
    
    def set_nome(self, nuovo_nome):
        self._nuovo_nome = nuovo_nome
    
    def set_nome(self, nuova_data_nascita):
        self._data_nascita = nuova_data_nascita
    
    def info(self):
        return f"Nome: {self.nome} (data di nascita: {self.data_nascita})"