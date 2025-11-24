# GESTIONE AULE SCOLASTICHE #

Il progetto è uno script Python che gestisce aule scolastiche (con studenti e professori), utilizzando i concetti dell'OOP.

---

## Funzionalità

Il programma permette di:
- creare aule identificate da un nome e una capienza massima.
- aggiungere studenti e professori.
- assegnare studenti e professori alle aule.
- visualizzare le informazioni di ogni aula.
- salvare ogni aula in un file "<nome_aula>.txt".

---

## Struttura del progetto

### Classe "Persona" (classe base)
- "nome"
- "data di nascita"

### Classe "Studente" (deriva da Persona)
Aggiunge:
- "matricola"

### Classe "Professore" (deriva da Persona)
Aggiunge:
- "materia" insegnata

### Classe "Aula"
Gestisce:
- nome aula
- capienza
- lista degli studenti: aggiunge e rimuove studenti
- professore assegnato: assegna professore
- mostra le info
- salva sul file "<nome_aula>.txt" le info

### Classe "GestoreAule"
- aggiune aule
- rimuove aule
- mostra le info delle aule esistenti
- trova una determinata aula

### File.txt
Viene creato un file per ogni aula con le seguenti info:
- nome aula
- capienza
- info professore
- info studenti (elencati)

---

## Main
Utilizza il match per:
1. crea aula
2. aggiungi studente
3. rimuovi studente
4. assegna professore
5. rimuovi aula
6. trova aula
7. mostra aule
8. salva tutte le aule su file
9. ucire

I vari dati sono richiesti in input dall'utente.
