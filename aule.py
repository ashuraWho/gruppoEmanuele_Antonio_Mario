from studente import Studente
from professore import Professore

class Aula:
    
    def __init__(self, nome: str, capienza: int):
        self.nome = nome # Nome aula
        self.capienza = capienza
        
        self.studenti = []      # Lista di Studente
        self.professore = None  # Professore assegnato (o None)

    def aggiungi_studente(self, studente: Studente):
        
        if studente in self.studenti: # Se ci sono studenti allora non aggiungerlo
            return False
        
        if len(self.studenti) >= self.capienza: # Se ce ne sono troppi allora non aggiungerlo
            return False
        
        self.studenti.append(studente)
        return True

    def rimuovi_studente(self, nome_studente: str):
        for s in self.studenti:
            if s.nome == nome_studente:
                self.studenti.remove(s)
                return True
            
        return False

    def assegna_professore(self, professore: Professore):
        self.professore = professore

    def mostra_info(self):
        print(f"\nAula: {self.nome}")
        print(f"Capienza: {self.capienza}")
        
        prof = self.professore.nome if self.professore else "Nessuno"
        
        print(f"Professore assegnato: {prof}")
        print(f"Studenti presenti ({len(self.studenti)}):")
        if self.studenti:
            for s in self.studenti:
                print(f"  - {s.nome} (data di nascita: {s.data_nascita})")
        else:
            print("Nessuno studente presente.")
            
    def salva_su_file(self): # Stampa le informazioni dell'aula in un file .txt
        nome_file = f"{self.nome}.txt"

        with open(nome_file, "w") as f:
            f.write(f"AULA: {self.nome}\n")
            f.write(f"Capienza: {self.capienza}\n\n")

            if self.professore:
                f.write("PROFESSORE:\n")
                f.write(self.professore.info() + "\n\n")
            else:
                f.write("PROFESSORE: nessuno\n\n")

            f.write("STUDENTI:\n")
            if not self.studenti:
                f.write("Nessuno studente presente.\n")
            else:
                for s in self.studenti:
                    f.write("- " + s.info() + "\n")

        print(f"File '{nome_file}' creato correttamente.")