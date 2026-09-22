"""
Autore: Lorenzo Airoldi
Data: 21/09/2026
Titolo: Quarto esercizio - Approssimazione del numero di Nepero (punto 4.a)

Input: numero intero N di termini da sommare.
Vincoli: N deve essere maggiore di zero.
Output: approssimazione di e con N termini: 1/0! + ... + 1/(N-1)!.
"""

# Funzioni
def fattoriale(n: int) -> int:
    """
    Calcola il fattoriale di un numero intero non negativo.
    Parametri formali: n (int), numero di cui calcolare il fattoriale, n >= 0.
    Valore di ritorno: int, fattoriale di n; per n = 0 restituisce 1.
    """
    risultato = 1  # Prodotto dei numeri da 1 a n
    for numero in range(1, n + 1):
        risultato = risultato * numero
    return risultato


def calcola_e(n: int) -> float:
    """
    Approssima e sommando n termini e richiamando la funzione fattoriale.
    Parametri formali: n (int), numero di termini, n > 0.
    Valore di ritorno: float, somma dei reciproci dei fattoriali da 0 a n-1.
    """
    somma = 0.0  # Somma dei termini della serie
    for numero in range(n):
        somma = somma + 1 / fattoriale(numero)
    return somma


# Programma principale: legge N e calcola l'approssimazione di e.
# Sezione di input dati
n = int(input("Numero di termini N: "))

# Inizializzazioni variabili
approssimazione = 0.0  # Valore approssimato del numero di Nepero

# Elaborazione
if n > 0:
    approssimazione = calcola_e(n)

# Sezione di output
if n > 0:
    print("Valore approssimato di e:", approssimazione)
else:
    print("N deve essere maggiore di zero.")
