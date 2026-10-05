"""
Autore: Lorenzo Airoldi
Data: 22/09/2026
Titolo: Liste - Dividere una lista in due parti

Input: una lista di interi e la lunghezza della prima parte.
Vincoli: lunghezza compresa tra zero e il numero di elementi della lista.
Output: prima e seconda parte, mantenendo l'ordine originale.
"""

# Funzioni
def dividi_lista(numeri: list, lunghezza: int) -> list:
    """
    Divide la lista senza modificare quella originale.
    Parametri formali: numeri (list), lunghezza (int) della prima parte.
    Valore di ritorno: list contenente due liste, prima e seconda parte.
    La validita' della lunghezza viene controllata nel programma principale.
    """
    return [numeri[:lunghezza], numeri[lunghezza:]]


# Programma principale: legge una lista e la divide alla posizione richiesta.
# Sezione di input dati
testo = input("Inserisci numeri interi separati da spazi: ")
lunghezza = int(input("Lunghezza della prima parte: "))

# Inizializzazioni variabili
numeri = []  # Lista originale
parti = []  # Lista contenente le due parti

# Elaborazione
for valore in testo.split():
    numeri.append(int(valore))

# Sezione di output
if lunghezza < 0 or lunghezza > len(numeri):
    print("La lunghezza deve essere compresa tra 0 e", len(numeri))
else:
    parti = dividi_lista(numeri, lunghezza)
    print("Prima parte:", parti[0])
    print("Seconda parte:", parti[1])
