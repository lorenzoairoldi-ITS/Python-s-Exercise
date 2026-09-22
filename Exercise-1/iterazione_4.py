"""
Autore: Lorenzo Airoldi
Data: 21/09/2026
Titolo: Iterazione - Quarto esercizio: minimo di N numeri

Input: quantita' N e gli N numeri da confrontare.
Vincoli: N deve essere un intero positivo.
Output: il minimo dei numeri inseriti.
"""

# Sezione di input dati
n = int(input("Quanti numeri vuoi inserire? "))

# Inizializzazioni variabili
minimo = 0

# Elaborazione e lettura dei numeri
if n > 0:
    minimo = float(input("Inserisci il primo numero: "))
    for i in range(n - 1):
        numero = float(input("Inserisci il numero successivo: "))
        if numero < minimo:
            minimo = numero

# Sezione di output
if n > 0:
    print("Il minimo e':", minimo)
else:
    print("La quantita' deve essere positiva.")
