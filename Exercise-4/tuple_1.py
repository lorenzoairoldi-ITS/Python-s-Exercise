"""
Autore: Lorenzo Airoldi
Data: 30/09/2026
Titolo: Tuple - Rimuovere l'n-esimo elemento

Input: la posizione da rimuovere da una tupla gia' definita nel codice.
Output: una nuova tupla senza l'elemento scelto.
Le posizioni indicate dall'utente partono da 1.
"""

# Funzioni
def rimuovi_elemento(elementi: tuple, posizione: int) -> tuple:
    """
    Costruisce una tupla senza l'elemento nella posizione richiesta.
    Parametri formali: elementi (tuple), tupla non vuota;
    posizione (int), posizione valida da 1 a len(elementi).
    Valore di ritorno: tuple, nuova tupla senza l'elemento scelto.
    """
    indice = posizione - 1  # Gli indici di Python partono da zero
    return elementi[:indice] + elementi[indice + 1:]


# Programma principale: rimuove un elemento dalla tupla di esempio.
# Inizializzazioni variabili
elementi = ('a', 'b', 'c', 'd')  # Tupla originale di stringhe

# Sezione di input dati
print("Tupla originale:", elementi)
posizione = int(input("Posizione da rimuovere (partendo da 1): "))
while posizione < 1 or posizione > len(elementi):
    posizione = int(input("Posizione non valida. Riprova: "))

# Elaborazione
risultato = rimuovi_elemento(elementi, posizione)

# Sezione di output
print("Tupla risultante:", risultato)
