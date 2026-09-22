"""
Autore: Lorenzo Airoldi
Data: 21/09/2026
Titolo: Selezione - Primo esercizio: equazione ax = b

Input: i coefficienti reali a e b.
Vincoli: si puo' dividere per a solo se a e' diverso da zero.
Output: soluzione, equazione impossibile oppure indeterminata.
"""

# Sezione di input dati
a = float(input("Inserisci a: "))
b = float(input("Inserisci b: "))

# Inizializzazioni variabili
x = 0
messaggio = ""

# Elaborazione
if a != 0:
    x = b / a
elif b == 0:
    messaggio = "Equazione indeterminata: ogni numero e' una soluzione."
else:
    messaggio = "Equazione impossibile: nessuna soluzione."

# Sezione di output
if a != 0:
    print("La soluzione e':", x)
else:
    print(messaggio)
