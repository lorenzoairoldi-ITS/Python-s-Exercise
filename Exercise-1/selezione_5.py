"""
Autore: Lorenzo Airoldi
Data: 21/09/2026
Titolo: Selezione - Quinto esercizio: sconto sulla spesa

Input: importo della spesa in euro.
Vincoli: importo non negativo. Sconto del 5% oltre 100 euro,
         del 10% oltre 300 euro; altrimenti nessuno sconto.
Output: importo effettivo da pagare.
"""

# Sezione di input dati
spesa = float(input("Inserisci l'importo della spesa: "))

# Inizializzazioni variabili
sconto = 0
totale = 0

# Elaborazione
if spesa >= 0:
    if spesa > 300:
        sconto = spesa * 10 / 100
    elif spesa > 100:
        sconto = spesa * 5 / 100
    totale = spesa - sconto

# Sezione di output
if spesa >= 0:
    print("Importo da pagare:", round(totale, 2), "euro")
else:
    print("La spesa non puo' essere negativa.")
