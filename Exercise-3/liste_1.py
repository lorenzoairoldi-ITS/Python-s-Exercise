"""
Autore: Lorenzo Airoldi
Data: 22/09/2026
Titolo: Liste - Rimuovere gli elementi duplicati

Input: numeri interi separati da spazi; invio senza numeri per una lista vuota.
Output: una lista senza duplicati, nell'ordine della prima comparsa.
"""

# Funzioni
def rimuovi_duplicati(numeri: list) -> list:
    """
    Copia ogni elemento solo alla sua prima comparsa, senza modificare l'input.
    Parametri formali: numeri (list), lista da esaminare.
    Valore di ritorno: list, nuova lista senza duplicati.
    """
    risultato = []  # Elementi gia' incontrati, senza ripetizioni
    for numero in numeri:
        if numero not in risultato:
            risultato.append(numero)
    return risultato


# Programma principale: legge una lista ed elimina le ripetizioni.
# Sezione di input dati
testo = input("Inserisci numeri interi separati da spazi: ")

# Inizializzazioni variabili
numeri = []  # Lista originale
risultato = []  # Lista senza duplicati

# Elaborazione
for valore in testo.split():
    numeri.append(int(valore))
risultato = rimuovi_duplicati(numeri)

# Sezione di output
print("Lista senza duplicati:", risultato)
