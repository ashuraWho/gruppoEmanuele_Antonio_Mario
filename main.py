from studente import Studente
from professore import Professore
from aule import Aula
from GestoreAule import GestoreAule

gestore = GestoreAule()

def crea_aula():
    nome = input("Nome aula: ")
    capienza = int(input("Capienza massima: "))
    aula = Aula(nome, capienza)
    gestore.aggiungi_aula(aula)
    print(f"Aula '{nome}' creata con capienza {capienza}.")

def aggiungi_studente_aula():
    nome_aula = input("Nome aula: ")
    aula = gestore.trova_aula(nome_aula)
    if not aula:
        print("Aula non trovata.")
        return

    nome = input("Nome studente: ")
    anno_nascita = int(input("Anno di nascita (es. 2003): "))
    matricola = input("Matricola: ")

    studente = Studente(nome, anno_nascita, matricola)
    if aula.aggiungi_studente(studente):
        print(f"Studente {nome} aggiunto all'aula {aula.nome}.")
    else:
        print("Non è stato possibile aggiungere lo studente.")

def rimuovi_studente_aula():
    nome_aula = input("Nome aula: ")
    aula = gestore.trova_aula(nome_aula)
    if not aula:
        print("Aula non trovata.")
        return

    matricola = input("Matricola dello studente da rimuovere: ")
    if aula.rimuovi_studente(matricola):
        print(f"Studente con matricola {matricola} rimosso dall'aula {aula.nome}.")
    else:
        print("Studente non trovato nell'aula.")

def assegna_professore_aula():
    nome_aula = input("Nome aula: ")
    aula = gestore.trova_aula(nome_aula)
    if not aula:
        print("Aula non trovata.")
        return

    nome = input("Nome professore: ")
    anno_nascita = int(input("Anno di nascita: "))
    materia = input("Materia insegnata: ")

    professore = Professore(nome, anno_nascita, materia)
    aula.assegna_professore(professore)
    print(f"Professore {nome} assegnato all'aula {aula.nome}.")

def rimuovi_aula():
    nome_aula = input("Nome aula da rimuovere: ")
    if gestore.rimuovi_aula(nome_aula):
        print(f"Aula '{nome_aula}' rimossa.")
    else:
        print("Aula non trovata.")

def trova_aula():
    nome_aula = input("Nome aula da cercare: ")
    aula = gestore.trova_aula(nome_aula)
    if aula:
        print(f"Aula trovata: {aula.nome}, capienza {aula.capienza}, studenti {len(aula.studenti)}.")
    else:
        print("Aula non trovata.")

def mostra_aule():
    gestore.mostra_aule()
    
def salva_aule_su_file():
    if not gestore.aule:
        print("Non ci sono aule da salvare.")
        return

    for aula in gestore.aule:
        aula.salva_su_file()
    print("Tutte le aule sono state salvate su file.")

def menu():
    while True:
        print("--- GESTIONE AULE ---")
        print("1. Crea aula")
        print("2. Aggiungi studente")
        print("3. Rimuovi studente")
        print("4. Assegna professore")
        print("5. Rimuovi aula")
        print("6. Trova aula")
        print("7. Mostra aule")
        print("8. Salva tutte le aule su file")
        print("9. Esci")

        scelta = input("Seleziona un'opzione: ")

        match scelta:
            case "1":
                crea_aula()
            case "2":
                aggiungi_studente_aula()
            case "3":
                rimuovi_studente_aula()
            case "4":
                assegna_professore_aula()
            case "5":
                rimuovi_aula()
            case "6":
                trova_aula()
            case "7":
                mostra_aule()
            case "8":
                salva_aule_su_file()
            case "9":
                print("Uscita.")
                break
            case _:
                print("Opzione non valida.")


if __name__ == "__main__":
    menu()
