from aule import Aula

class GestoreAule:
    def __init__(self):
        self.aule = []  # Lista di oggetti Aula
        
    
    def aggiungi_aula(self, aula: Aula):
        self.aule.append(aula)
        
    def rimuovi_aula(self, nome: str):
        
        for aula in self.aule:
            if aula.nome == nome:
                self.aule.remove(aula)
                return True
        return False
    
    def mostra_aule(self):
        
        print("-" * 30)
        for aula in self.aule:
            
            aula.mostra_info()
            print("-" * 30)
            
    def trova_aula(self, nome: str) -> Aula:
        
        for aula in self.aule:
            if aula.nome == nome:
                return aula
            
        return None

