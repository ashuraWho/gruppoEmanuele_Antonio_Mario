from studente import Studente
from professore import Professore
from aule import Aula
from gestoreAule import GestoreAule

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
        print("Non è stato possibile aggiungere lo studente (capienza o duplicato).")

def assegna_professore_aula():
    nome_aula = input("Nome aula: ")
    aula = gestore.trova_aula(nome_aula)
    if not aula:
        print("Aula non trovata.")
        return

    nome = input("Nome professore: ")
    anno_nascita = int(input("Anno di nascita (es. 1980): "))
    materia = input("Materia insegnata: ")

    professore = Professore(nome, anno_nascita, materia)
    aula.assegna_professore(professore)
    print(f"Professore {nome} assegnato all'aula {aula.nome}.")

def mostra_aule():
    gestore.mostra_aule()

def menu():
    while True:
        print("\n--- GESTIONE AULE ---")
        print("1. Crea aula")
        print("2. Aggiungi studente")
        print("3. Assegna professore")
        print("4. Mostra aule")
        print("5. Esci")

        scelta = input("Seleziona un'opzione: ")

        match scelta:
            case "1":
                crea_aula()
            case "2":
                aggiungi_studente_aula()
            case "3":
                assegna_professore_aula()
            case "4":
                mostra_aule()
            case "5":
                print("Uscita dal programma.")
                break
            case _:
                print("Opzione non valida.")

if __name__ == "__main__":
    menu()
