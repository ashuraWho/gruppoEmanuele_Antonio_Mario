"""
    
    Implemento tutta la logica per definire una persona:
        - studenti
        - professori
    
"""

class Person: # Classe base
    def __init__(self, name, eta):
        self._name = name
        self._eta = eta

    def assign_eta(self, eta):
        self._eta = eta

    def get_name(self): # Leggere il nome
        return self._eta
    
    def get_name(self): # Leggere il nome
        return self._eta

# ---------------------------------------------------------------

class Studente(Person): # Classe figlio di "Person" (per gli studenti)
    def __init__(self, name, ruolo):
        super().__init__(name)
        
        self.ruolo = ruolo # Studente

class Professore(Person): # Classe figlio di "Person" (per i Professori)
    def __init__(self, name, ruolo):
        super().__init__(name)
        
        self.ruolo = ruolo # Professore