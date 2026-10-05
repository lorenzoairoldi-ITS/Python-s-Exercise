"""
Autore: Lorenzo Airoldi
Data: 30/09/2026
Titolo: Tuple - Invertire una tupla

Input: una tupla di esempio definita nel codice, senza input da tastiera.
Output: una nuova tupla con gli elementi in ordine inverso.
"""

# Funzioni
def inverti_tupla(elementi: tuple) -> tuple:
    """
    Inserisce ogni elemento all'inizio di una nuova tupla.
    Parametri formali: elementi (tuple), tupla da invertire.
    Valore di ritorno: tuple, elementi in ordine inverso.
    """
    risultato = ()  # Tupla che raccoglie gli elementi in ordine inverso
    for elemento in elementi:
        risultato = (elemento,) + risultato
    return risultato


# Programma principale: inverte l'ordine della tupla di esempio.
# Inizializzazioni variabili
elementi = ('a', 'c', 'f')  # Tupla originale proposta nel PDF

# Elaborazione
risultato = inverti_tupla(elementi)

# Sezione di output
print("Tupla originale:", elementi)
print("Tupla invertita:", risultato)
