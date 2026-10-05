"""
Autore: Lorenzo Airoldi
Data: 30/09/2026
Titolo: Tuple - Sostituire l'ultimo valore delle liste

Input: un numero intero da inserire nelle liste della tupla di esempio.
Output: la tupla con l'ultimo elemento di ogni lista sostituito.
Le liste vuote vengono lasciate invariate perche' non hanno un ultimo elemento.
"""

# Funzioni
def sostituisci_ultimi(elementi: tuple, valore: int) -> tuple:
    """
    Modifica l'ultimo elemento delle liste non vuote contenute nella tupla.
    Parametri formali: elementi (tuple), tupla con liste e altri valori;
    valore (int), nuovo valore da assegnare.
    Valore di ritorno: tuple, la stessa tupla con le liste modificate.
    """
    for elemento in elementi:
        if isinstance(elemento, list) and len(elemento) > 0:
            elemento[-1] = valore
    return elementi


# Programma principale: usa la tupla proposta nel PDF.
# Sezione di input dati
valore = int(input("Inserisci il nuovo valore intero: "))

# Inizializzazioni variabili
elementi = ([10, 20, 40], 'a', [40, 50, 60], 23, [70, 80, 90])

# Elaborazione
print("Tupla originale:", elementi)
risultato = sostituisci_ultimi(elementi, valore)

# Sezione di output
print("Tupla risultante:", risultato)
