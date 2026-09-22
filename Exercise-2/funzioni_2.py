"""
Autore: Lorenzo Airoldi
Data: 21/09/2026
Titolo: Secondo esercizio - Somma dei pari e prodotto dei dispari

Input: un numero arbitrario di interi passati direttamente alla funzione.
Vincoli: nessun input da tastiera; la parita' viene valutata su numeri interi.
Output: somma dei numeri pari e prodotto dei numeri dispari.
In assenza di pari la somma e' 0; in assenza di dispari il prodotto e' 1.
"""

# Funzioni
def somma_pari_prodotto_dispari(*numeri: int) -> tuple:
    """
    Somma i numeri pari e moltiplica i numeri dispari.
    Parametri formali: numeri, un numero arbitrario di valori int.
    Valore di ritorno: tuple di due int, somma dei pari e prodotto dei dispari.
    """
    somma = 0  # Accumulatore della somma dei numeri pari
    prodotto = 1  # Accumulatore del prodotto dei numeri dispari

    for numero in numeri:
        if numero % 2 == 0:
            somma = somma + numero
        else:
            prodotto = prodotto * numero

    return somma, prodotto


# Programma principale: usa valori di esempio senza input da tastiera.
# Inizializzazioni variabili
somma_pari = 0  # Risultato della somma
prodotto_dispari = 1  # Risultato del prodotto

# Elaborazione: i dati sono passati direttamente alla funzione.
somma_pari, prodotto_dispari = somma_pari_prodotto_dispari(1, 2, 3, 4, 5, 6)

# Sezione di output
print("Somma dei numeri pari:", somma_pari)
print("Prodotto dei numeri dispari:", prodotto_dispari)
