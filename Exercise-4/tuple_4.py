"""
Autore: Lorenzo Airoldi
Data: 30/09/2026
Titolo: Tuple - Contare gli elementi prima di una tupla

Input: una lista di esempio definita nel programma.
Output: il numero di elementi che precedono la prima tupla.
Se non ci sono tuple, vengono contati tutti gli elementi della lista.
"""

# Funzioni
def conta_prima_tupla(elementi: list) -> int:
    """
    Conta gli elementi della lista fermandosi alla prima tupla, esclusa.
    Parametri formali: elementi (list), lista da esaminare.
    Valore di ritorno: int, numero di elementi prima della prima tupla.
    """
    conteggio = 0  # Numero di elementi incontrati prima della tupla
    for elemento in elementi:
        if isinstance(elemento, tuple):
            break
        conteggio = conteggio + 1
    return conteggio


# Programma principale: conta gli elementi prima della tupla nella lista.
# Sezione di input dati
elementi = [10, 'ciao', 3.5, (1, 2), 40, 'fine']  # Lista da esaminare

# Inizializzazioni variabili
risultato = 0  # Numero di elementi prima della prima tupla

# Elaborazione
risultato = conta_prima_tupla(elementi)

# Sezione di output
print("Lista:", elementi)
print("Elementi prima della prima tupla:", risultato)
