"""
Autore: Lorenzo Airoldi
Data: 21/09/2026
Titolo: Selezione - Terzo esercizio
Scrivere un programma che legga il raggio r di una circonferenza
e ne calcoli l'area e la lunghezza.

Input: il raggio r, espresso come numero reale.
Vincoli: il raggio non puo' essere negativo; con r = 0 i risultati sono zero.
Output: area del cerchio e lunghezza della circonferenza.
"""

from math import pi

# Sezione di input dati
r = float(input("Inserisci il raggio (numero): ").replace(",", "."))

# Inizializzazioni variabili
area = 0
lunghezza = 0

# Elaborazione
if r >= 0:
    area = pi * r * r
    lunghezza = 2 * pi * r

# Sezione di output
if r >= 0:
    print("Area del cerchio:", area)
    print("Lunghezza della circonferenza:", lunghezza)
else:
    print("Il raggio non puo' essere negativo.")
