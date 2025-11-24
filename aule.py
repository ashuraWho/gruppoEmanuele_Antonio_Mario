from studente import Studente
from professore import Professore

class Aula:
    
    def __init__(self, nome: str, capienza: int):
        self.nome = nome
        self.capienza = capienza
        self.studenti = []
        self.professore = None

    def aggiungi_studente(self, studente: Studente):
        # Controllo che lo studente non sia già presente (per matricola)
        for s in self.studenti:
            if s.matricola == studente.matricola:
                return False

        # Controllo capienza
        if len(self.studenti) >= self.capienza:
            return False
        
        self.studenti.append(studente)
        return True

    def rimuovi_studente(self, matricola_studente: str):
        for s in self.studenti:
            if s.matricola == matricola_studente:
                self.studenti.remove(s)
                return True
        return False

    def assegna_professore(self, professore: Professore):
        self.professore = professore

    def mostra_info(self):
        print(f"\nAula: {self.nome}")
        print(f"Capienza: {self.capienza}")

        if self.professore:
            print(f"Professore assegnato: {self.professore.nome} ({self.professore.materia})")
        else:
            print(f"Professore assegnato: Nessuno")

        print(f"Studenti presenti ({len(self.studenti)}):")
        if self.studenti:
            for s in self.studenti:
                print(f"  - Nome: {s.nome} | Matricola: {s.matricola} | Data di nascita: {s.data_nascita}")
        else:
            print("  Nessuno studente presente.")
            
    def salva_su_file(self): # Stampa le informazioni dell'aula in un file .txt
        nome_file = f"{self.nome}.txt"

        with open(nome_file, "w") as f:
            f.write(f"AULA: {self.nome}\n")
            f.write(f"Capienza: {self.capienza}\n\n")

            # Professore
            if self.professore:
                f.write("PROFESSORE:\n")
                f.write(self.professore.info() + "\n\n")
            else:
                f.write("PROFESSORE: nessuno\n\n")

            # Studenti
            f.write("STUDENTI:\n")
            if not self.studenti:
                f.write("Nessuno studente presente.\n")
            else:
                for s in self.studenti:
                    f.write("- " + s.info() + "\n")

        print(f"File '{nome_file}' creato correttamente.")