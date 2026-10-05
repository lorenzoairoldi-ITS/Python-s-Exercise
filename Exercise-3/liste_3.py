"""
Autore: Lorenzo Airoldi
Data: 22/09/2026
Titolo: Liste - Trovare il secondo numero piu' piccolo

Input: una lista di numeri interi separati da spazi.
Output: il secondo valore distinto piu' piccolo, se presente.
Interpretazione: le ripetizioni del minimo non contano come secondo minimo.
"""

# Funzioni
def secondo_minimo(numeri: list):
    """
    Elimina le ripetizioni, ordina i valori e seleziona il secondo.
    Parametri formali: numeri (list), lista di interi non modificata dalla funzione.
    Valore di ritorno: int, secondo valore distinto in ordine crescente,
    oppure None se ci sono meno di due valori distinti.
    """
    distinti = []  # Valori della lista senza ripetizioni
    for numero in numeri:
        if numero not in distinti:
            distinti.append(numero)
    if len(distinti) < 2:
        return None
    distinti.sort()
    return distinti[1]


# Programma principale: legge una lista e cerca il secondo minimo distinto.
# Sezione di input dati
testo = input("Inserisci numeri interi separati da spazi: ")

# Inizializzazioni variabili
numeri = []  # Numeri da confrontare
risultato = None  # Secondo minimo; None indica che non esiste

# Elaborazione
for valore in testo.split():
    numeri.append(int(valore))
risultato = secondo_minimo(numeri)

# Sezione di output
if risultato is None:
    print("Servono almeno due numeri distinti.")
else:
    print("Secondo numero piu' piccolo:", risultato)
